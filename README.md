# 🚀 Fast API with File Upload on UI

> A full-stack web application featuring a modern React frontend with an intuitive file upload interface and a robust Python FastAPI backend for seamless file handling.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61dafb.svg)](https://react.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

This project is a production-ready full-stack application that demonstrates best practices for handling file uploads in a web application. It combines:

- **Frontend**: React with responsive UI components for file uploads
- **Backend**: FastAPI with efficient file processing and validation
- **Integration**: Seamless communication between client and server

## ✨ Features

- 📁 **File Upload**: Drag-and-drop and click-to-upload functionality
- 🔄 **Data Processing**: Handle multiple file formats (CSV, Parquet, JSON, etc.)
- ⚡ **Fast Performance**: Async file processing with FastAPI
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🔒 **Validation**: Comprehensive file validation and error handling
- 📊 **Real-time Feedback**: Progress tracking and status updates

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Server**: Uvicorn
- **Key Libraries**:
  - `pandas` - Data processing
  - `python-multipart` - File form handling
  - `pytz` - Timezone support

### Frontend
- **Framework**: React
- **Language**: JavaScript/JSX
- **Styling**: CSS3 (Responsive)
- **HTTP Client**: Fetch API

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js 14 or higher
- pip and npm/yarn package managers

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/waterisverywet/Fast-api-with-file-upload-on-UI.git
   cd Fast-api-with-file-upload-on-UI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory**
   ```bash
   cd frontend  # or your frontend directory
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```
   The app will open at `http://localhost:3000`

## 📖 API Documentation

Once the FastAPI server is running, access the interactive API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Key Endpoints

#### Upload File
```http
POST /upload/
Content-Type: multipart/form-data

Body:
  file: <file_object>
```

**Response**: `200 OK`
```json
{
  "filename": "data.csv",
  "size": 1024,
  "status": "success",
  "message": "File uploaded successfully"
}
```

## 📁 Project Structure

```
Fast-api-with-file-upload-on-UI/
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── __pycache__/              # Python cache (auto-generated)
├── README.md                 # This file
└── frontend/                 # React frontend (structure may vary)
    ├── src/
    ├── public/
    ├── package.json
    └── ...
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory (optional):

```env
# FastAPI
API_HOST=0.0.0.0
API_PORT=8000

# File Upload
MAX_FILE_SIZE=10485760  # 10MB in bytes
ALLOWED_EXTENSIONS=csv,json,parquet,xlsx

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

## 📦 Dependencies

All Python dependencies are listed in `requirements.txt`. Key packages:

```
fastapi>=0.95.0
uvicorn[standard]>=0.21.0
python-multipart>=0.0.5
pandas>=1.5.0
pytz>=2023.3
```

Install with:
```bash
pip install -r requirements.txt
```

## 🧪 Testing

### Manual Testing

1. Open the frontend application
2. Use the file upload interface to select or drag files
3. Monitor the backend console for processing details
4. Check the API responses in the browser console

### API Testing with cURL

```bash
curl -X POST "http://localhost:8000/upload/" \
  -H "accept: application/json" \
  -F "file=@path/to/your/file.csv"
```

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Change the port in main.py or use:
python main.py --port 8001
```

**CORS Errors**
- Ensure the frontend URL is in the `CORS_ORIGINS` configuration
- Check that both servers are running

**File Upload Fails**
- Verify file size is within limits
- Check file format is allowed
- Ensure proper permissions on upload directory

## 🚀 Deployment

### Deploy Backend

**Using Heroku**
```bash
heroku create your-app-name
git push heroku master
```

**Using Docker**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Deploy Frontend

**Using Vercel/Netlify**
```bash
npm run build
# Deploy the `build` folder
```

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [File Upload Best Practices](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
- [Python Real Python Guide](https://realpython.com/)

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**waterisverywet**
- GitHub: [@waterisverywet](https://github.com/waterisverywet)

## 🙏 Acknowledgments

- FastAPI community for the excellent framework
- React team for the powerful UI library
- All contributors and users who have provided feedback

## 📞 Support

If you have questions or need help:

1. Check the [Documentation](#-api-documentation)
2. Search [GitHub Issues](https://github.com/waterisverywet/Fast-api-with-file-upload-on-UI/issues)
3. Create a new issue with detailed information

---

**Made with ❤️ by [waterisverywet](https://github.com/waterisverywet)**

*Last Updated: 2026*
