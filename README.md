<div id="top"></div>
<div align="center">

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
  <a href="https://github.com/Thorin-the-Bearded/Hospitality/">
    <h1>Hospitality</h1>
  </a>

  <h3 align="center">The Hospital Management System, created by TON Tech.</h3>
  
  <hr>
  
  <p align="center">
    A comprehensive hospital management system developed by TON Tech, created by Thorin-the-Bearded and team.
    <br />
    <a href="https://github.com/Thorin-the-Bearded/Hospitality/"><strong>View Source Code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Thorin-the-Bearded/Hospitality/issues">Report Bug</a>
    ·
    <a href="https://github.com/Thorin-the-Bearded/Hospitality/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-hospitality">Running Hospitality</a></li>
      </ul>
    </li>
    <li><a href="#the-basics-of-hospitality">The Basics of Hospitality</a></li>
    <ul>
        <li><a href="#login-screen">Login Screen</a></li>
        <li><a href="#registration">Registration</a></li>
        <li><a href="#home-screen">Home Screen</a></li>
        <li><a href="#visitor-features">Visitor Features</a></li>
        <li><a href="#patient-features">Patient Features</a></li>
        <li><a href="#staff-features">Staff Features</a></li>
        <li><a href="#logging-out">Logging Out</a></li>
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Hospitality is a comprehensive hospital management system developed by TON Tech, a team of three university students: Thorin, Obert, and Nikolai. The system aims to streamline and enhance various hospital operations and processes, providing an efficient and user-friendly solution.

Features:
* User Authentication: The system includes a login screen with options for visitors, patients, and staff. Staff members can select their role during the login process.
* Registration: New users can easily register by creating a unique username and password.
* Visitor Information: The app displays essential hospital information, such as services offered, facilities available, and contact details, providing visitors with a user-friendly and intuitive experience.
* Patient Management: Staff members can efficiently manage patient information, including personal details, medical history, and assigned rooms.
* Appointment Scheduling: The system enables staff members to schedule appointments with patients, check doctor availability, and manage appointment status and notifications.
* Medical Record Management: Robust features for managing medical records, including secure file uploads, access controls, versioning, and efficient storage.
* Prescription Tracking: Doctors can easily create and manage prescriptions for patients, including medication details, dosage instructions, and refill tracking.
* Billing Integration: Seamless integration with a payment gateway provider, generating invoices based on provided services and tracking payment status and notifications.
* Analytics for Patient Satisfaction: A flexible survey creation module allows customization of questions, storing survey responses, and generating analytics and reports.
* CRM Functionality: Staff management features, including adding, editing, and removing staff members, managing hospital departments, equipment, and inventory, and assigning roles and permissions.
* Staff-Specific Features: Tailored features for doctors, nurses, administrative staff, and management staff, enabling efficient execution of their respective responsibilities.
* Database Optimization and Performance Tuning: Analysis and optimization of database queries, implementation of indexes for improved performance, and fine-tuning for efficient operations.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django 4](https://www.djangoproject.com/)
* [Python 3](https://www.python.org/)
* [SQL Lite 3](https://sqlite.org/index.html)
* HTML
* CSS

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Setting up Hospitality might sound daugnting, but not to fear - as long as README is here!
Simply follow these steps, as you would the doctors instructions.

### Installation

1. Install Python:
   - Visit the official Python website: [https://www.python.org](https://www.python.org)
   - Download the latest version of Python for your operating system.
   - Follow the installation instructions provided by Python to complete the installation.

2. Install Django:
   - Open a command prompt or terminal.
   - Run the following command to install Django using pip:
     ```sh
     pip install Django
     ```

3. Navigate to the directory where you would like to install Hospitality:
   ```sh
   cd [DirectoryPathHere]
   ```

4. Clone the repository by entering the following command into your shell:
   ```sh
   git clone https://github.com/Thorin-the-Bearded/Hospitality.git
   ```

5. Create a virtual environment by entering the following command:
   ```sh
   virtualenv hospitalityEnv
   ```

6. Activate the virtual environment by entering the appropriate command based on your operating system:
   - For Windows:
     ```sh
     hospitalityEnv\Scripts\activate
     ```
   - For macOS/Linux:
     ```sh
     source hospitalityEnv/bin/activate
     ```

7. Install the required dependencies by running the following command:
   ```sh
   pip install -r requirements.txt
   ```

8. Apply database migrations by running the following command:
   ```sh
   python manage.py migrate
   ```

### Running Hospitality

To start the server and run Hospitality locally, follow these steps:

1. Run the server with the following command:
   ```sh
   python manage.py runserver
   ```

2. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000/](http://localhost:8000/) to access the Hospitality application.

Please note that SQLite is the default database used by Django, and it is included in the project's codebase. Therefore, there is no need to separately install SQLite. The database file will be automatically created and configured when running the migration command.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## The Basics of Hospitality

## Hospital Management System

### Login Screen
The app features a login screen where users can choose their role and sign in accordingly.

#### Visitor Login
Visitors can log in using their credentials to access limited information and functionalities.

#### Patient Login
Patients can log in using their credentials to access their personal medical information, appointments, and other relevant features.

#### Staff Login
Staff members can log in using their credentials and select their role to access different functionalities based on their position within the hospital.

### Registration
If it's the user's first time using the app, they will be redirected to the registration page. Here, they can create a username and password that meet the minimum requirements.

### Home Screen
After logging in, users will be directed to the home screen, which serves as the main view of the app.

### Visitor Features
Visitors will have access to limited information about the hospital, such as general services, contact details, visiting hours, and other relevant visitor-related information.

### Patient Features
Patients will have access to the following features:

#### Patient Profile
Patients can view and update their personal information, including contact details, medical history, allergies, and other relevant information.

#### Appointments
Patients can schedule, view, and manage their appointments with doctors or other healthcare professionals.

#### Medical Records
Patients can access and manage their medical records, including test results, diagnoses, treatments, and prescriptions.

#### Billing
Patients can view and manage their billing information, including invoices, payments, and insurance details.

### Staff Features
Staff members will have access to the following features:

#### Role Selection
Staff members can choose their role within the hospital, such as doctor, nurse, administrator, or other positions, to access specific functionalities tailored to their responsibilities.

#### Patient Management
Staff members can search for and manage patient information, including demographics, medical history, appointments, and records.

#### Appointment Scheduling
Staff members can schedule and manage appointments for patients, ensuring proper coordination and availability of healthcare professionals.

#### Medical Record Management
Staff members can view, update, and manage patient medical records, including diagnoses, treatments, prescriptions, and other relevant information.

#### Billing and Insurance
Staff members can handle billing and insurance-related tasks, such as generating invoices, processing payments, and verifying insurance coverage.

#### Analytics and Reporting
Staff members can access analytics and generate reports related to patient satisfaction, appointment statistics, billing data, and other relevant metrics.

### Logging Out
Users can log out of the app to ensure the security of their data and prevent unauthorized access.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Phase 1: Project Setup and Database Initialization
    - [ ] Install Python and Django.
    - [ ] Set up a virtual environment.
    - [ ] Create a new Django project.
    - [ ] Choose and install the appropriate database system (e.g., SQLite 3.42.0).
    - [ ] Configure database settings in Django's configuration.
    - [ ] Set up database migrations and create the necessary tables:
        - [ ] User Table
            - [ ] id (AutoField)
            - [ ] username (CharField)
            - [ ] email (EmailField)
            - [ ] password (CharField)
        - [ ] Patient Table
            - [ ] id (AutoField)
            - [ ] first_name (CharField)
            - [ ] last_name (CharField)
            - [ ] date_of_birth (DateField)
            - [ ] gender (CharField)
            - [ ] contact_number (CharField)
            - [ ] address (TextField)
        - [ ] MedicalHistory Table
            - [ ] id (AutoField)
            - [ ] patient_id (ForeignKey to Patient table)
            - [ ] medical_condition (CharField)
            - [ ] treatment (TextField)
            - [ ] start_date (DateField)
            - [ ] end_date (DateField)
        - [ ] Appointment Table
            - [ ] id (AutoField)
            - [ ] patient_id (ForeignKey to Patient table)
            - [ ] doctor_id (ForeignKey to User table)
            - [ ] appointment_date (DateTimeField)
            - [ ] status (CharField)
        - [ ] MedicalRecord Table
            - [ ] id (AutoField)
            - [ ] patient_id (ForeignKey to Patient table)
            - [ ] record_file (FileField)
            - [ ] uploaded_at (DateTimeField)
        - [ ] Prescription Table
            - [ ] id (AutoField)
            - [ ] patient_id (ForeignKey to Patient table)
            - [ ] doctor_id (ForeignKey to User table)
            - [ ] medication_name (CharField)
            - [ ] dosage (CharField)
            - [ ] instructions (TextField)
            - [ ] prescribed_date (DateField)
            - [ ] refills_remaining (IntegerField)
        - [ ] Department Table
            - [ ] id (AutoField)
            - [ ] name (CharField)
            - [ ] description (TextField)
        - [ ] Equipment Table
            - [ ] id (AutoField)
            - [ ] name (CharField)
            - [ ] description (TextField)
            - [ ] quantity (IntegerField)
            - [ ] available (BooleanField)
        - [ ] Inventory Table
            - [ ] id (AutoField)
            - [ ] name (CharField)
            - [ ] description (TextField)
            - [ ] quantity (IntegerField)
            - [ ] expiration_date (DateField)

- [ ] Phase 2: User Management
    - [ ] Create user models and database tables.
    - [ ] Implement user registration functionality:
        - [ ] Design user registration form UI.
        - [ ] Implement form validation and error handling.
        - [ ] Store user data in the database.
    - [ ] Develop user login and logout views.
    - [ ] Build user profile management features:
        - [ ] Design user profile UI.
        - [ ] Implement profile update functionality.

- [ ] Phase 3: Visitor Information and Basic UI
    - [ ] Create views and templates to display general hospital information.
    - [ ] Design intuitive and user-friendly UI/UX for visitors.
    - [ ] Implement navigation menus and page layouts.

- [ ] Phase 4: Basic Search Functionality
    - [ ] Develop search forms for patients.
    - [ ] Implement search functionality for patients:
        - [ ] Implement search queries to retrieve patient information.
        - [ ] Display search results with relevant patient details.
        - [ ] Provide search filters to refine results.

- [ ] Phase 5: Display Patient's Room Information
    - [ ] Implement a feature to retrieve and display the assigned room number for a patient.
    - [ ] Link the room information to the patient's profile or search result.

- [ ] Phase 6: Hospital Map Integration
    - [ ] Research and integrate with a mapping service or library.
    - [ ] Develop a hospital map feature that displays the layout and facilities of the hospital:
        - [ ] Enable visitors to access the hospital map.
        - [ ] Integrate the hospital map feature with the patient search results.

- [ ] Phase 7: Patient Management
    - [ ] Design patient registration form UI.
    - [ ] Implement form validation and error handling.
    - [ ] Store patient data in the database.
    - [ ] Create medical history models and database tables.
    - [ ] Develop UI for viewing and updating medical history.
    - [ ] Implement data validation and access controls.

- [ ] Phase 8: Appointment Scheduling
    - [ ] Design appointment booking form UI.
    - [ ] Implement form validation and error handling.
    - [ ] Check doctor availability based on schedules.
    - [ ] Store appointment data in the database.
    - [ ] Create views for staff to view and update appointment status.
    - [ ] Implement appointment status updates and notifications.

- [ ] Phase 9: Medical Record Management
    - [ ] Design database schema for storing medical records.
    - [ ] Implement file upload functionality for medical records.
    - [ ] Set up secure storage for medical records.
    - [ ] Create views and templates for displaying and updating medical records.
    - [ ] Implement access controls and permissions for record management.
    - [ ] Add versioning and auditing for record modifications.
    - [ ] Research and integrate with a medical imaging system API.
    - [ ] Develop functionality for accessing and displaying diagnostic images.

- [ ] Phase 10: Prescription Tracking
    - [ ] Design prescription form UI for doctors.
    - [ ] Implement form validation for prescriptions.
    - [ ] Store prescription data in the database.
    - [ ] Develop views for patients to request prescription refills.
    - [ ] Implement reminders for prescription refills.

- [ ] Phase 11: Billing Integration
    - [ ] Research and choose a payment gateway provider.
    - [ ] Integrate the selected payment gateway into the system.
    - [ ] Design invoice templates and generate invoices based on services provided.
    - [ ] Implement payment tracking and notifications.

- [ ] Phase 12: Analytics for Patient Satisfaction
    - [ ] Develop a survey creation form with customizable questions.
    - [ ] Implement data validation for survey responses.
    - [ ] Store survey responses in the database.
    - [ ] Design and create a dashboard UI for displaying analytics.
    - [ ] Implement data visualization and generate reports based on survey data.

- [ ] Phase 13: CRM Functionality
    - [ ] Design UI for adding, editing, and removing staff members.
    - [ ] Implement staff registration and user management features.
    - [ ] Set up roles and permissions for staff members.
    - [ ] Create views and templates for managing hospital departments.
    - [ ] Implement functionality to add, edit, and delete departments.
    - [ ] Associate staff members with specific departments.
    - [ ] Design UI for adding and managing hospital equipment.
    - [ ] Implement CRUD functionality for hospital equipment.

- [ ] Phase 14: Performance Optimization and Testing
    - [ ] Identify and optimize slow-performing database queries.
    - [ ] Implement caching mechanisms for frequently accessed data.
    - [ ] Perform load testing and optimize system performance.
    - [ ] Implement automated tests to ensure system stability and functionality.

- [ ] Phase 15: Deployment and Launch
    - [ ] Set up a production server environment.
    - [ ] Configure deployment scripts and processes.
    - [ ] Migrate the database to the production server.
    - [ ] Configure web server settings and SSL certificate.
    - [ ] Perform final system testing in the production environment.
    - [ ] Launch the hospital management system.


See the [open issues](https://github.com/Thorin-the-Bearded/Hospitality/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU-3.0 License. See [LICENSE](https://github.com/Thorin-the-Bearded/Hospitality/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
This project is created by TON Tech:

* [Thorin](https://github.com/Thorin-the-Bearded)
* [Obert](https://github.com/obertgwamure)
* [Nikolai](https://github.com/NikhirMG)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Thorin-the-Bearded/Hospitality.svg?style=for-the-badge&color=a81313
[contributors-url]: https://github.com/Thorin-the-Bearded/Hospitality/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Thorin-the-Bearded/Hospitality.svg?style=for-the-badge&color=a81313
[forks-url]: https://github.com/Thorin-the-Bearded/Hospitality/network/members
[stars-shield]: https://img.shields.io/github/stars/Thorin-the-Bearded/Hospitality.svg?style=for-the-badge&color=a81313
[stars-url]: https://github.com/Thorin-the-Bearded/Hospitality/stargazers
[issues-shield]: https://img.shields.io/github/issues/Thorin-the-Bearded/Hospitality.svg?style=for-the-badge&color=a81313
[issues-url]: https://github.com/Thorin-the-Bearded/Hospitality/issues
[license-shield]: https://img.shields.io/github/license/Thorin-the-Bearded/Hospitality.svg?style=for-the-badge&color=a81313
[license-url]: https://github.com/Thorin-the-Bearded/Hospitality/blob/master/LICENSE
