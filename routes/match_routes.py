"""
Match-related routes for Tennis Analytics Platform
"""
from flask import Blueprint, render_template, flash, redirect, url_for, request, abort, send_file
from flask_login import login_required, current_user
import json
import os
import tempfile
from datetime import datetime
from werkzeug.utils import secure_filename
from app import db
from models import Match, MatchStatistic
from forms import MatchUploadForm, ExcelUploadForm
from helpers import process_match_data, process_excel_data
from utils import calculate_overall_score, generate_match_analysis
from routes.utils import check_match_access, get_template_date
import google.generativeai as genai
from flask import jsonify
import os
from datetime import datetime

# 配置 Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # 从环境变量获取 API 密钥
genai.configure(api_key=GEMINI_API_KEY)


# Create blueprint
match_bp = Blueprint('match', __name__)

@match_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_match():
    """Match upload route"""
    form = MatchUploadForm()
    excel_form = ExcelUploadForm()
    
    # Process match upload form
    if form.validate_on_submit() and 'user_score' in request.form:
        # Create new match
        match = Match(
            title=form.title.data,
            date=form.date.data,
            opponent=form.opponent.data,
            location=form.location.data,
            description=form.description.data,
            user_score=form.user_score.data,
            opponent_score=form.opponent_score.data,
            match_result=form.match_result.data,
            user_id=current_user.id
        )
        
        db.session.add(match)
        db.session.commit()
        
        # Process uploaded files if any
        if form.files.data and any(f.filename for f in form.files.data):
            try:
                stats = process_match_data(form.files.data, match.id)
                
                # Save statistics
                for stat_type, stat_data in stats.items():
                    statistic = MatchStatistic(
                        statistic_type=stat_type,
                        statistic_data=json.dumps(stat_data),
                        match_id=match.id
                    )
                    db.session.add(statistic)
                
                db.session.commit()
                flash('Match data processed successfully!', 'success')
            except Exception as e:
                flash(f'Error processing match data: {str(e)}', 'danger')
        
        flash('Match uploaded successfully!', 'success')
        return redirect(url_for('match.analysis', match_id=match.id))
    
    # Process Excel upload form
    if excel_form.validate_on_submit() and 'title' in request.form and 'excel_file' in request.files:
        # Create new match with basic info
        match = Match(
            title=excel_form.title.data,
            date=datetime.utcnow(),
            user_id=current_user.id
        )
        
        db.session.add(match)
        db.session.commit()
        
        # Process Excel file
        try:
            stats = process_excel_data(excel_form.excel_file.data, match.id)
            
            # Update match with extracted information if any
            if 'match_info' in stats:
                info = stats.pop('match_info')
                match.date = info.get('date', match.date)
                match.opponent = info.get('opponent', None)
                match.location = info.get('location', None)
                match.user_score = info.get('user_score', None)
                match.opponent_score = info.get('opponent_score', None)
                match.match_result = info.get('match_result', None)
                db.session.commit()
            
            # Save statistics
            for stat_type, stat_data in stats.items():
                statistic = MatchStatistic(
                    statistic_type=stat_type,
                    statistic_data=json.dumps(stat_data),
                    match_id=match.id
                )
                db.session.add(statistic)
            
            db.session.commit()
            flash('Excel data processed successfully!', 'success')
        except Exception as e:
            flash(f'Error processing Excel data: {str(e)}', 'danger')
            db.session.delete(match)
            db.session.commit()
            return render_template('upload.html', form=form, excel_form=excel_form, **get_template_date())
        
        flash('Match uploaded and processed successfully!', 'success')
        return redirect(url_for('match.analysis', match_id=match.id))
    
    return render_template('upload.html', form=form, excel_form=excel_form, **get_template_date())

@match_bp.route('/analysis/<int:match_id>')
@login_required
def analysis(match_id):
    """Match analysis route"""
    # Check if user has access to this match
    match = check_match_access(match_id)
    
    # Get all statistics
    statistics = {}
    for stat in match.statistics.all():
        statistics[stat.statistic_type] = stat.get_data()
    
    # Calculate overall performance score
    overall_score = calculate_overall_score(statistics)
    
    # Generate match analysis
    match_analysis = generate_match_analysis(statistics)
    
    return render_template(
        'analysis.html',
        match=match,
        statistics=statistics,
        overall_score=overall_score,
        match_analysis=match_analysis,
        **get_template_date()
    )

@match_bp.route('/match/<int:match_id>')
@login_required
def match_details(match_id):
    """Match details route"""
    # Check if user has access to this match
    match = check_match_access(match_id)
    
    # Get all statistics
    statistics = {}
    for stat in match.statistics.all():
        statistics[stat.statistic_type] = stat.get_data()
    
    return render_template(
        'match_details.html',
        match=match,
        statistics=statistics,
        **get_template_date()
    )

@match_bp.route('/match/<int:match_id>/report')
@login_required
def download_report(match_id):
    """Download full match report route"""
    # Check if user has access to this match
    match = check_match_access(match_id)
    
    # Get all statistics
    statistics = {}
    for stat in match.statistics.all():
        statistics[stat.statistic_type] = stat.get_data()
    
    # Calculate overall performance score
    overall_score = calculate_overall_score(statistics)
    
    # Generate match analysis
    match_analysis = generate_match_analysis(statistics)
    
    # Create HTML report
    html = render_template(
        'match_report.html',
        match=match,
        statistics=statistics,
        overall_score=overall_score,
        match_analysis=match_analysis,
        export_mode=True,
        **get_template_date()
    )
    
    # Create a temporary file to store the HTML report
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp:
        temp.write(html.encode('utf-8'))
        temp_name = temp.name
    
    # Generate filename
    date_str = match.date.strftime('%Y-%m-%d')
    filename = f"{date_str}_tennis_match_report_{match.id}.html"
    
    return send_file(
        temp_name,
        mimetype='text/html',
        download_name=filename,
        as_attachment=True
    )



# 在 match_bp 中添加新的路由
@match_bp.route('/match/<int:match_id>/analyze', methods=['POST'])
@login_required
def analyze_match(match_id):
    """AI analysis route for match"""
    # 检查访问权限
    match = check_match_access(match_id)
    
    # 获取统计数据
    statistics = {}
    for stat in match.statistics.all():
        statistics[stat.statistic_type] = stat.get_data()
    
    try:
        # 初始化 Gemini 模型
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # 构建提示词
        prompt = f"""
        As a professional tennis coach, analyze these match statistics and provide specific improvement recommendations.
        Focus on the most important areas that need improvement.

        Match Information:
        - Date: {match.date}
        - Opponent: {match.opponent}
        - Location: {match.location}
        - Result: {match.match_result}

        Key Statistics:
        1. Serve Performance:
           - First Serve %: {statistics.get('basic_stats', {}).get('first_serve_percentage')}%
           - Aces: {statistics.get('basic_stats', {}).get('aces')}
           - Double Faults: {statistics.get('basic_stats', {}).get('double_faults')}

        2. Shot Analysis:
           - Forehand Winners/Errors: {statistics.get('shot_analysis', {}).get('forehand', {}).get('winners')}/{statistics.get('shot_analysis', {}).get('forehand', {}).get('errors')}
           - Backhand Winners/Errors: {statistics.get('shot_analysis', {}).get('backhand', {}).get('winners')}/{statistics.get('shot_analysis', {}).get('backhand', {}).get('errors')}

        3. Movement:
           - Distance Covered: {statistics.get('player_movement', {}).get('distance_covered')}m
           - Direction Changes: {statistics.get('player_movement', {}).get('direction_changes')}

        Please provide:
        1. Key areas needing improvement (based on statistics)
        2. Specific practice drills for each area
        3. Technical tips for improvement

        Format the response in a clear, structured way with numbered points.
        Keep the recommendations practical and actionable.
        """
        
        # 获取 AI 分析
        response = model.generate_content(prompt)
        
        # 返回分析结果
        return jsonify({
            "success": True,
            "analysis": response.text,
            "timestamp": datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        # 记录错误
        print(f"AI Analysis Error: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to generate analysis. Please try again later."
        }), 500