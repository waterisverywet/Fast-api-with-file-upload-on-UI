# Contributing to Fast API with File Upload on UI

First off, thank you for considering contributing to this project! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem** in as much detail as possible
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**
- **Include your environment details** (OS, Python version, Node version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python and JavaScript style guides
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

## Development Setup

### Prerequisites

- Python 3.9+
- Node.js 14+
- Git

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Fast-api-with-file-upload-on-UI.git
   cd Fast-api-with-file-upload-on-UI
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up the backend**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Set up the frontend** (if applicable)
   ```bash
   cd frontend
   npm install
   cd ..
   ```

5. **Run tests**
   ```bash
   # Run backend tests
   pytest
   
   # Run frontend tests
   cd frontend
   npm test
   ```

## Style Guides

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these additions:

- Maximum line length: 100 characters
- Use type hints where possible
- Document all public functions with docstrings
- Use meaningful variable names

```python
def process_file(file_path: str) -> dict:
    """
    Process a file and return its metadata.
    
    Args:
        file_path: Path to the file to process
        
    Returns:
        Dictionary containing file metadata
    """
    pass
```

### JavaScript/React Style Guide

- Use ES6+ syntax
- Use meaningful variable and function names
- Add JSDoc comments for components and functions
- Use functional components with hooks
- Proper prop validation with PropTypes

```javascript
/**
 * FileUpload component for handling file uploads
 * @param {Function} onFileSelect - Callback when file is selected
 * @returns {JSX.Element}
 */
const FileUpload = ({ onFileSelect }) => {
  // Component code
};
```

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Consider starting the commit message with an applicable emoji:
  - 🎨 `:art:` - Improve structure/format of the code
  - 🐛 `:bug:` - Fix a bug
  - ✨ `:sparkles:` - Introduce new features
  - 📝 `:memo:` - Add or update documentation
  - 🚀 `:rocket:` - Deploy stuff
  - ✅ `:white_check_mark:` - Add tests
  - 🔧 `:wrench:` - Add or update configuration files

### Example Commit Messages

```
✨ Add file drag-and-drop functionality to upload component
🐛 Fix CORS error when uploading files
📝 Update API documentation for file upload endpoint
✅ Add unit tests for file validation
```

## Testing

### Writing Tests

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Use descriptive test names

### Running Tests

```bash
# Backend tests
pytest --cov=. --cov-report=html

# Frontend tests
cd frontend
npm test -- --coverage
```

## Documentation

- Update README.md if you change functionality
- Add docstrings to all public functions
- Update API documentation if endpoints change
- Include comments for complex logic

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on

### Project Roadmap

We maintain a project roadmap in the Projects section. Check it out to see what we're working on and what's planned for future releases.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project acknowledgments

---

**Thank you for contributing to Fast API with File Upload on UI! 🎉**
