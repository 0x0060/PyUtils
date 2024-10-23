import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Any, Dict
from pyutils.logger.log import Logger


class SerializationError(Exception):
    pass


class DeserializationError(Exception):
    pass


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, data: Any) -> str:
        pass

    @abstractmethod
    def deserialize(self, string: str) -> Any:
        pass


class JsonSerializer(BaseSerializer):
    def serialize(self, data: Any) -> str:
        try:
            json_data = json.dumps(data, default=str)
            Logger.info("Successfully serialized data to JSON.")
            return json_data
        except (TypeError, ValueError) as e:
            Logger.error(f"Failed to serialize data to JSON: {e}")
            raise SerializationError(f"Failed to serialize data to JSON: {e}")

    def deserialize(self, json_string: str) -> Any:
        try:
            data = json.loads(json_string)
            Logger.info("Successfully deserialized data from JSON.")
            return data
        except (json.JSONDecodeError, TypeError) as e:
            Logger.error(f"Failed to deserialize data from JSON: {e}")
            raise DeserializationError(f"Failed to deserialize data from JSON: {e}")


class XmlSerializer(BaseSerializer):
    def serialize(self, data: Dict[str, Any], root_tag: str = 'root') -> str:
        try:
            root = ET.Element(root_tag)
            self._dict_to_xml(data, root)
            xml_string = ET.tostring(root, encoding='unicode')
            Logger.info("Successfully serialized data to XML.")
            return xml_string
        except Exception as e:
            Logger.error(f"Failed to serialize data to XML: {e}")
            raise SerializationError(f"Failed to serialize data to XML: {e}")

    def deserialize(self, xml_string: str) -> Dict[str, Any]:
        try:
            root = ET.fromstring(xml_string)
            data = self._xml_to_dict(root)
            Logger.info("Successfully deserialized data from XML.")
            return data
        except ET.ParseError as e:
            Logger.error(f"Failed to deserialize data from XML: {e}")
            raise DeserializationError(f"Failed to deserialize data from XML: {e}")

    @staticmethod
    def _dict_to_xml(data: Dict[str, Any], parent: ET.Element) -> None:
        for key, value in data.items():
            if isinstance(value, dict):
                child = ET.SubElement(parent, key)
                XmlSerializer._dict_to_xml(value, child)
            elif isinstance(value, list):
                for item in value:
                    item_elem = ET.SubElement(parent, key)
                    if isinstance(item, dict):
                        XmlSerializer._dict_to_xml(item, item_elem)
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
                data[child.tag] = XmlSerializer._xml_to_dict(child)
            else:
                data[child.tag] = child.text
        return data
