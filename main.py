from datetime import datetime
import os


def backup_docker_compose(input_dir, output_dir):
    combined_content = ""

    # Walk through the directory
    for root, dirs, files in os.walk(input_dir):
        if 'docker-compose.yml' in files:
            file_path = os.path.join(root, 'docker-compose.yml')
            with open(file_path, 'r') as file:
                combined_content += '#///////////////////////////////////////////////////////////////////////\n'
                combined_content += '#///////////////////////////////////////////////////////////////////////\n'
                combined_content += '#                       New Docker-Compose File\n'
                combined_content += '#///////////////////////////////////////////////////////////////////////\n'
                combined_content += '#///////////////////////////////////////////////////////////////////////\n\n\n'
                combined_content += file.read() + "\n\n"

        # Create the output directory if it does not exist
        os.makedirs(output_dir, exist_ok=True)

        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y_%H-%M")
        # Define the output file path
        output_file_path = os.path.join(output_dir, f'backup_docker_compose_{current_time}.yml')

        # Write the combined content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(combined_content)


input_directory = r'C:\Users\Home Server\Desktop\docker_configs'
output_directory = r'C:\Users\Home Server\Desktop\docker_configs'

backup_docker_compose(input_directory, output_directory)
