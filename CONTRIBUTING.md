# Contributing to AI-Powered Root Cause Analysis System

Thank you for your interest in contributing to the AI-Powered Root Cause Analysis System! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Docker Desktop
- [Ollama](https://ollama.ai) with Phi-4-mini model
- Python 3.11+ (for local development)
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vivek1251/ai-rca-system.git
   cd ai-rca-system
   ```

2. **Pull the required LLM model**
   ```bash
   ollama pull phi4-mini
   ```

3. **Start the development environment**
   ```bash
   docker-compose up -d
   ```

4. **For local Python development** (optional)
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r app/requirements.txt
   pip install -r rca_service/requirements.txt
   ```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Test the application:
```bash
# Simulate errors
curl http://localhost:5000/cause-error
curl http://localhost:5000/stress

# Get AI root cause analysis
curl http://localhost:8000/rca
```

## 📝 Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused on single responsibilities

## 🔄 Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### PR Requirements
- All tests pass
- Code is well-documented
- Follows the existing code style
- Includes appropriate tests for new features
- Updates documentation if needed

## 🐛 Reporting Issues

When reporting bugs, please include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, Docker version)
- Relevant logs or screenshots

## 📚 Documentation

- Update README.md for significant changes
- Add docstrings for new functions
- Update API documentation for endpoint changes

## 🤝 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:
- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

## 🙋 Questions?

If you have questions about contributing, feel free to open an issue or contact the maintainers.

Thank you for contributing! 🎉