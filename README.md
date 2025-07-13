# 🚗 Parking Lot Management System  
*A Django-based web application built during a technical internship at Vehinova.*

## 🧠 Overview
The **Parking Lot Management System** is a user-friendly platform that allows users to:
- View available parking spots (Bike, Car, EV Car).
- Reserve spots for a specified duration.
- Automatically manage spot availability based on real-time reservations.

## 🛠️ Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (Bootstrap + Custom styling)
- **Database**: SQLite
- **Authentication**: Django’s built-in user model
- **Static Management**: Django Staticfiles

## 📁 Project Structure
```
suryaakkala-parking-lot-managent-system/
│
├── manage.py                  
├── db.sqlite3                 
├── parkinglot/               # Project-level configuration
│   └── settings.py, urls.py, ...
├── parkingapp/               # Core application
│   ├── models.py             
│   ├── views.py              
│   ├── urls.py               
│   ├── management/commands/update_spots.py
│   ├── templates/parkingapp/*.html
│   ├── templates/registration/login.html
│   └── static/
├── staticfiles/              
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview
```

## ✅ Key Features
- **Login System**: Secure user authentication using Django’s login view.
- **Live Availability**: Spot availability updates in real-time based on active reservations.
- **Reservation System**: Custom duration reservation system.
- **Command-line Utility**: `update_spots.py` for syncing availability.
- **Visual UI**: Responsive, animated UI with video and background images.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/parking-lot-system.git
cd parking-lot-system
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

### 6. Update Spot Status (Optional)
```bash
python manage.py update_spots
```

## 🔐 Login Credentials
Use the superuser you created or register via the login page.

## 🌐 URLs
- `/accounts/login/` → Login
- `/` → Home
- `/spots/<spot_type>/` → Spot List
- `/reserve/<spot_id>/` → Reservation

## 🎨 Screenshots
(Add screenshots here if needed)

## 🏢 Internship Acknowledgment
Built during the **Technical Internship** at **Vehinova**.

## 🧑‍💻 Team
This project was developed as part of a collaborative team effort under the **Vehinova Technical Internship**.
Led by **Surya Akkala**, with contributions from the following team members:
| Name             | GitHub                                 | Role              |
|------------------|----------------------------------------|-------------------|
| **A. Hari Kailash** | [@harianchala](https://github.com/harianchala) | Frontend Developer |
| **G. Karuna Sri** | [@Karunasri921](https://github.com/Karunasri921) | Frontend Developer |
| **K. Sathvik**    | [@Sathvik](https://github.com/sathvik) | Backend Developer |
| **K. Sruthi** | [@Sruthi-3-0](https://github.com/Sruthi-3-0) | Frontend Developer |
| **P. Rishitha** | [@2200032932](https://github.com/2200032932) | Frontend Developer |
| **Surya Akkala** | [@suryaakkala](https://github.com/suryaakkala) | Team Lead / Backend |
| **Y. Ravi Kumar** | [@yarrapothuravi](https://github.com/yarrapothuravi) | Frontend Developer |


## 📜 License
This project is for educational/demo purposes only.
