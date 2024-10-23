import re
from typing import Optional
from pyutils.logger.log import Logger


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Validator:
    """A class providing static methods for common input validations."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate an email address."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            Logger.error(f"Invalid email address: {email}")
            raise ValidationError(f"Invalid email address: {email}")
        Logger.info(f"Valid email: {email}")
        return True

    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """Validate a phone number (10 digits)."""
        pattern = r'^\d{10}$'
        if not re.match(pattern, phone):
            Logger.error(f"Invalid phone number: {phone}")
            raise ValidationError(f"Invalid phone number: {phone}")
        Logger.info(f"Valid phone: {phone}")
        return True

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Validate a URL."""
        pattern = r'^(http|https)://[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}'
        if not re.match(pattern, url):
            Logger.error(f"Invalid URL: {url}")
            raise ValidationError(f"Invalid URL: {url}")
        Logger.info(f"Valid URL: {url}")
        return True

    @staticmethod
    def is_valid_username(username: str) -> bool:
        """Validate a username (alphanumeric, 3-20 characters)."""
        pattern = r'^[a-zA-Z0-9]{3,20}$'
        if not re.match(pattern, username):
            Logger.error(f"Invalid username: {username}")
            raise ValidationError(f"Invalid username: {username}")
        Logger.info(f"Valid username: {username}")
        return True

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """Validate a password (minimum 8 characters, at least one letter and one number)."""
        if (len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password)):
            Logger.error("Invalid password: must be at least 8 characters long and include at least one letter and one number.")
            raise ValidationError("Invalid password: must be at least 8 characters long and include at least one letter and one number.")
        Logger.info(f"Valid password.")
        return True

    @staticmethod
    def is_valid_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
        """Validate a date string against a specific format."""
        try:
            from datetime import datetime
            datetime.strptime(date_str, date_format)
        except ValueError:
            Logger.error(f"Invalid date: {date_str}. Expected format: {date_format}.")
            raise ValidationError(f"Invalid date: {date_str}. Expected format: {date_format}.")
        Logger.info(f"Valid date: {date_str}.")
        return True

    @staticmethod
    def is_valid_ip(ip: str) -> bool:
        """Validate an IP address (IPv4 or IPv6)."""
        ipv4_pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        ipv6_pattern = r'^[\da-fA-F]{1,4}(:[\da-fA-F]{1,4}){7}$'
        if re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip):
            Logger.info(f"Valid IP address: {ip}.")
            return True
        Logger.error(f"Invalid IP address: {ip}.")
        raise ValidationError(f"Invalid IP address: {ip}")

    @staticmethod
    def is_valid_postal_code(postal_code: str, country: Optional[str] = None) -> bool:
        """Validate postal codes for different formats."""
        if country == 'US':
            pattern = r'^\d{5}(-\d{4})?$'
        else:
            pattern = r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$'
        if not re.match(pattern, postal_code):
            Logger.error(f"Invalid postal code for {country}: {postal_code}.")
            raise ValidationError(f"Invalid postal code for {country}: {postal_code}")
        Logger.info(f"Valid postal code for {country}: {postal_code}.")
        return True

    @staticmethod
    def is_valid_credit_card(card_number: str) -> bool:
        """Validate credit card numbers using the Luhn algorithm."""
        def luhn_check(num: str) -> bool:
            total = 0
            reverse_digits = num[::-1]
            for i, digit in enumerate(reverse_digits):
                n = int(digit)
                if i % 2 == 1:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            return total % 10 == 0
        
        pattern = r'^\d{16}$'
        if re.match(pattern, card_number) and luhn_check(card_number):
            Logger.info(f"Valid credit card number: {card_number}.")
            return True
        Logger.error(f"Invalid credit card number: {card_number}.")
        raise ValidationError(f"Invalid credit card number: {card_number}")

    @staticmethod
    def is_valid_ssn(ssn: str) -> bool:
        """Validate US Social Security Numbers."""
        pattern = r'^\d{3}-\d{2}-\d{4}$'
        if not re.match(pattern, ssn):
            Logger.error(f"Invalid Social Security Number: {ssn}.")
            raise ValidationError(f"Invalid Social Security Number: {ssn}")
        Logger.info(f"Valid SSN: {ssn}.")
        return True

    @staticmethod
    def sanitize_string(input_str: str) -> str:
        """Sanitize input string to remove potential harmful characters."""
        sanitized = re.sub(r'[^\w\s-]', '', input_str).strip()
        Logger.info(f"Sanitized string: '{sanitized}'.")
        return sanitized
