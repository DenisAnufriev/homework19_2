# homework19_2
## Project Description


## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DenisAnufriev/homework19_2.git
cd DenisAnufriev_homework19_2
```
### 2. Install Dependencies
The project uses Pip for dependency management.
```bash
pip install -r requirements.txt
```
### 3. Start Migrations
To start migrations, use the following command:
```bash
python3 manage.py migrate
```

### 4. Load Fixture
Loading test fixtures for the database:
```bash
python3 manage.py load_fixtures
```
### 5. Run the Project
To start the server, use the following command:
```bash
python3 manage.py runserver
```
The server will be available at http://127.0.0.1:8000