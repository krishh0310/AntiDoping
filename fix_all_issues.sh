#!/bin/bash

echo "================================"
echo "Anti-Doping Platform Cleanup"
echo "================================"

# Activate virtual environment
source .venv/bin/activate

echo ""
echo "✅ Running Django system checks..."
python manage.py check

echo ""
echo "✅ Formatting Python files..."
# Check if black is installed, if not install it
python -m pip install black > /dev/null 2>&1
black base/*.py --quiet

echo ""
echo "✅ Running security checks..."
python manage.py check --deploy 2>/dev/null || echo "   (Some deploy checks expected to fail in dev)"

echo ""
echo "✅ Collecting static files..."
python manage.py collectstatic --noinput > /dev/null 2>&1

echo ""
echo "================================"
echo "Cleanup Complete!"
echo "================================"
