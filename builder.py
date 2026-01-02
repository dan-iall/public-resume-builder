import json
import os
import subprocess
import sys
from datetime import datetime

from jinja2 import Template

VERSIONS_DIR = 'cv_versions'


def build_version(version_name):
    version_path = os.path.join(VERSIONS_DIR, version_name)
    if not os.path.isdir(version_path):
        print(f"Error: Version '{version_name}' not found at {version_path}")
        return

    print(f'--- Building Version: {version_name} ---')

    # Paths
    json_path = os.path.join(version_path, 'resume_data.json')
    template_path = os.path.join(version_path, 'resume_template.qmd.j2')
    # Intermediate output
    intermediate_qmd_path = os.path.join(version_path, 'resume.qmd')
    intermediate_pdf_path = os.path.join(version_path, 'resume.pdf')

    # Read Data
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'  Error: resume_data.json not found in {version_path}')
        return

    # Extract Meta for Naming
    meta = data.get('meta', {})
    company = meta.get('company', 'general').lower().replace(' ', '-')
    role = meta.get('role', 'resume').lower().replace(' ', '-')

    # Date handling: Use provided date or current date, format to YYYY-MM
    date_str = meta.get('date', datetime.now().strftime('%Y-%m-%d_%H%M'))
    try:
        # If full date provided, try to truncate to YYYY-MM
        if len(date_str) > 7:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            date_str = date_obj.strftime('%Y-%m')
    except ValueError:
        pass  # Keep as is if parsing fails, or assume it's already correct format

    # Construct Target Filename
    # Pattern: cv_dani_[company]_[role]_[YYYY-MM].pdf
    target_filename = f'resume_{company}_{role}_{date_str}.pdf'
    target_pdf_path = os.path.join(version_path, target_filename)

    # Read Template
    try:
        with open(template_path, 'r') as f:
            template_str = f.read()
    except FileNotFoundError:
        print(f'  Error: resume_template.qmd.j2 not found in {version_path}')
        return

    # Render Template
    template = Template(template_str)
    rendered_content = template.render(**data)

    # Write QMD
    with open(intermediate_qmd_path, 'w') as f:
        f.write(rendered_content)
    print(f'  Generated {intermediate_qmd_path}')

    # Run Quarto
    try:
        # Force Quarto to use the current python environment
        env = os.environ.copy()
        # Use the currently running python executable
        env['QUARTO_PYTHON'] = sys.executable

        subprocess.run(
            ['quarto', 'render', 'resume.qmd'], cwd=version_path, check=True, env=env
        )
        print(f'  Successfully rendered PDF for {version_name}')

        # Rename to target filename
        if os.path.exists(intermediate_pdf_path):
            os.rename(intermediate_pdf_path, target_pdf_path)
            print(f'  Renamed to: {target_filename}')
        else:
            print(f'  Warning: Expected output {intermediate_pdf_path} not found.')

    except subprocess.CalledProcessError as e:
        print(f'  Error rendering PDF for {version_name}: {e}')


def main():
    # If specific version arg provided
    if len(sys.argv) > 1:
        target_versions = sys.argv[1:]
    else:
        # Build all subdirectories in cv_versions
        target_versions = [
            d
            for d in os.listdir(VERSIONS_DIR)
            if os.path.isdir(os.path.join(VERSIONS_DIR, d))
        ]

    for version in target_versions:
        build_version(version)


if __name__ == '__main__':
    main()
