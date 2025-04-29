
Built by https://www.blackbox.ai

---

# Electronic Invoice System

## Project Overview

The Electronic Invoice System is a web application designed for creating, managing, and sending electronic invoices in Arabic. It provides a user-friendly interface to handle individual and batch invoicing processes, ensuring compliance with tax regulations.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/electronic-invoice-system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd electronic-invoice-system
   ```

3. **Open the HTML files in your browser**:
   - Open `login.html` to begin using the application.

This project does not require any additional installations, as it is a static HTML project.

## Usage

- **Login Page**: Start by logging into the system using `login.html`.
- **Create Invoices**: Navigate to `electronic-invoice.html` to create and customize invoices.
- **Batch Invoices**: Use `batch-invoices.html` to create multiple invoices simultaneously.
- **View Sent Invoices**: Go to `sent-invoices.html` to view all sent invoices and filter them by date or invoice number.
- **Configuration**: Configure your account settings and taxpayer information in `portal-config.html`.

## Features

- **Responsive Design**: The application works well on different screen sizes thanks to Tailwind CSS.
- **Arabic Language Support**: All text is displayed in Arabic, making it user-friendly for Arabic-speaking users.
- **Dynamic Invoice Calculation**: Automatically calculates totals and tax amounts based on user input.
- **Batch Processing**: Allows users to generate and send multiple invoices at once.
- **Invoice History**: Users can view previously sent invoices and filter them based on various criteria.

## Dependencies

This project primarily relies on the following libraries:
- [Tailwind CSS](https://tailwindcss.com/) for styling.
- [Font Awesome](https://fontawesome.com/) for icons.

These libraries are included via CDN links in the HTML files.

## Project Structure

The project consists of the following files:

```
/electronic-invoice-system
├── batch-invoices.html         # Page to create and send multiple invoices.
├── electronic-invoice.html     # Page to create a single electronic invoice.
├── login.html                  # User login page.
├── portal-config.html          # Page for portal settings and taxpayer information.
├── sent-invoices.html          # Page to view and filter sent invoices.
```

### Features of Each Page

- **`login.html`**: User authentication and login interface.
- **`electronic-invoice.html`**: Form for creating an individual invoice with item management.
- **`batch-invoices.html`**: Allows addition and sending of multiple invoices at once, including functionality for loading ranges.
- **`sent-invoices.html`**: Display previously sent invoices with filtering options.
- **`portal-config.html`**: Configuration settings for client ID, secrets, and taxpayer information.

## Conclusion

The Electronic Invoice System is a comprehensive tool for managing invoices electronically, streamlining the process for users and ensuring compliance with taxation practices. For further modifications and feature updates, users are encouraged to explore the code and adapt it according to their needs.