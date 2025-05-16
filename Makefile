.PHONY: test test-utils test-selenium clean

# 默认的 Python 解释器
PYTHON = python3

# Flask 应用的端口
PORT = 5000

# 启动 Flask 应用（在后台运行）
start-flask:
	@echo "Starting Flask application..."
	@$(PYTHON) app.py &
	@sleep 2  # 等待 Flask 应用启动

# 停止 Flask 应用
stop-flask:
	@echo "Stopping Flask application..."
	@pkill -f "python app.py" || true

# 运行所有测试
test: start-flask
	@echo "Running all tests..."
	@pytest test_utils.py -v
	@pytest selenium_tests/test_homepage.py -v
	@pytest selenium_tests/test_login_page.py -v
	@make stop-flask

# 只运行单元测试
test-utils:
	@echo "Running unit tests..."
	@pytest test_utils.py -v

# 只运行 Selenium 测试
test-selenium: start-flask
	@echo "Running Selenium tests..."
	@pytest selenium_tests/test_homepage.py -v
	@pytest selenium_tests/test_login_page.py -v
	@make stop-flask

# 清理 Python 缓存文件
clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name ".pytest_cache" -exec rm -r {} + 