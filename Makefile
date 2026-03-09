.PHONY: install run clean

install:
	pip install -r requirements.txt

run:
	streamlit run dashboard_app.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete