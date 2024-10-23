import os
import subprocess
from pyutils.logger.logger import Logger


class DocGenerator:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def generate_docs(self, output_dir: str = "docs") -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            Logger.info(f"Created documentation directory: {output_dir}")

        Logger.info("Generating documentation...")
        
        try:
            subprocess.run(["sphinx-apidoc", "-o", output_dir, "."], check=True)
            subprocess.run(["make", "html"], cwd=output_dir, check=True)
            Logger.info("Documentation generated successfully.")
        except subprocess.CalledProcessError as e:
            Logger.error(f"Failed to generate documentation: {e}")
