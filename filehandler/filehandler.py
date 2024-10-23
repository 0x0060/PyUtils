import csv
import json
import os
import xml.etree.ElementTree as ET
import yaml
import toml
from typing import Any, Dict, List, Union
from pyutils.logger.log import Logger


class FileHandlingError(Exception):
    pass


class BaseFileHandler:
    def read(self, file_path: str) -> Any:
        pass

    def write(self, file_path: str, data: Any) -> None:
        pass


class JsonFileHandler(BaseFileHandler):
    def read(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileHandlingError(f"File not found: {file_path}")
        
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                Logger.info(f"Successfully read JSON file: {file_path}")
                return data
        except (json.JSONDecodeError, IOError) as e:
            Logger.error(f"Failed to read JSON file: {e}")
            raise FileHandlingError(f"Failed to read JSON file: {e}")

    def write(self, file_path: str, data: Dict[str, Any]) -> None:
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
                Logger.info(f"Successfully wrote JSON file: {file_path}")
        except IOError as e:
            Logger.error(f"Failed to write JSON file: {e}")
            raise FileHandlingError(f"Failed to write JSON file: {e}")


class CsvFileHandler(BaseFileHandler):
    def read(self, file_path: str) -> List[Dict[str, Any]]:
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileHandlingError(f"File not found: {file_path}")

        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                Logger.info(f"Successfully read CSV file: {file_path}")
                return data
        except (csv.Error, IOError) as e:
            Logger.error(f"Failed to read CSV file: {e}")
            raise FileHandlingError(f"Failed to read CSV file: {e}")

    def write(self, file_path: str, data: List[Dict[str, Any]]) -> None:
        if not data:
            Logger.warning("No data provided to write to CSV.")
            return

        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
                Logger.info(f"Successfully wrote CSV file: {file_path}")
        except IOError as e:
            Logger.error(f"Failed to write CSV file: {e}")
            raise FileHandlingError(f"Failed to write CSV file: {e}")


class XmlFileHandler(BaseFileHandler):
    def read(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileHandlingError(f"File not found: {file_path}")

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = self._xml_to_dict(root)
            Logger.info(f"Successfully read XML file: {file_path}")
            return data
        except ET.ParseError as e:
            Logger.error(f"Failed to read XML file: {e}")
            raise FileHandlingError(f"Failed to read XML file: {e}")

    def write(self, file_path: str, data: Dict[str, Any], root_tag: str = 'root') -> None:
        try:
            root = ET.Element(root_tag)
            self._dict_to_xml(data, root)
            tree = ET.ElementTree(root)
            tree.write(file_path)
            Logger.info(f"Successfully wrote XML file: {file_path}")
        except Exception as e:
            Logger.error(f"Failed to write XML file: {e}")
            raise FileHandlingError(f"Failed to write XML file: {e}")

    @staticmethod
    def _dict_to_xml(data: Dict[str, Any], parent: ET.Element) -> None:
        for key, value in data.items():
            if isinstance(value, dict):
                child = ET.SubElement(parent, key)
                XmlFileHandler._dict_to_xml(value, child)
            elif isinstance(value, list):
                for item in value:
                    item_elem = ET.SubElement(parent, key)
                    if isinstance(item, dict):
                        XmlFileHandler._dict_to_xml(item, item_elem)
                    else:
                        item_elem.text = str(item)
            else:
                child = ET.SubElement(parent, key)
                child.text = str(value)

    @staticmethod
    def _xml_to_dict(element: ET.Element) -> Dict[str, Any]:
        data = {}
        for child in element:
            if len(child) > 0:
                data[child.tag] = XmlFileHandler._xml_to_dict(child)
            else:
                data[child.tag] = child.text
        return data


class YamlFileHandler(BaseFileHandler):
    def read(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileHandlingError(f"File not found: {file_path}")

        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
                Logger.info(f"Successfully read YAML file: {file_path}")
                return data
        except (yaml.YAMLError, IOError) as e:
            Logger.error(f"Failed to read YAML file: {e}")
            raise FileHandlingError(f"Failed to read YAML file: {e}")

    def write(self, file_path: str, data: Dict[str, Any]) -> None:
        try:
            with open(file_path, 'w') as file:
                yaml.dump(data, file)
                Logger.info(f"Successfully wrote YAML file: {file_path}")
        except IOError as e:
            Logger.error(f"Failed to write YAML file: {e}")
            raise FileHandlingError(f"Failed to write YAML file: {e}")


class TomlFileHandler(BaseFileHandler):
    def read(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            Logger.error(f"File not found: {file_path}")
            raise FileHandlingError(f"File not found: {file_path}")

        try:
            with open(file_path, 'r') as file:
                data = toml.load(file)
                Logger.info(f"Successfully read TOML file: {file_path}")
                return data
        except (toml.TomlDecodeError, IOError) as e:
            Logger.error(f"Failed to read TOML file: {e}")
            raise FileHandlingError(f"Failed to read TOML file: {e}")

    def write(self, file_path: str, data: Dict[str, Any]) -> None:
        try:
            with open(file_path, 'w') as file:
                toml.dump(data, file)
                Logger.info(f"Successfully wrote TOML file: {file_path}")
        except IOError as e:
            Logger.error(f"Failed to write TOML file: {e}")
            raise FileHandlingError(f"Failed to write TOML file: {e}")
