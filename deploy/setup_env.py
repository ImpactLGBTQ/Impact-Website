#!/usr/bin/env python3

import subprocess

# python script desgined to prepare the enviroment of a fresh production server, or update it



log_file = NotImplemented
warnings = 0
errors = 0  
failed = []

def main():
     # Display startup message
    print("==============================\nSetting up enviroment for the Impact website")
    # Setup packages
    setup_packages()

    

# Setup the enviroments packages
def setup_packages():
    # setup nginx
    print("------------------------------\nStarting nginx install and configuration...")
    print('Checking if nginx is already installed...')
    if check_if_installed('nginx'):
        # If the package is already installed
        print('nginx is already installed. Moving on')
    else:
        # If its not
        print('nginx is not installed. Installing...')
        if not install_pkg('nginx'):
            # If installing nginx failed
            print('nginx install failed!')
            # Increase the erros count and add nginx
            errors += 1
            failed.append('nginx - Failed to install')

    print('nginx install done. Configuring', end='\n\n')

    # Postgre
    postgre_name = 'postgresql-10'
    print('------------------------------\nStarting postgresql install and configuration...')
    print('Checking if postgre-sql is already installed')
    if check_if_installed(postgre_name):
        print('postgre-sql already installed. Moving on')
    else:
        print('postgre-sql not installed. Installing...')
        if not install_pkg(postgre_name):
            print('Failed to install postgre-sql!')
            # Increase error count and add postgre
            errors += 1
            failed.append('postgresql - Failed to install')
    
    

# Check if a package exists  
def check_if_installed(pkg_name : str) -> bool:
    log_file.write('=================== INSTALL CHECK FOR: {} ===================\n'.format(pkg_name.upper()))
    log_file.flush()
    try:
        status = subprocess.check_call(('dpkg', '-s', pkg_name,), stderr=log_file, stdout=log_file)
    except subprocess.CalledProcessError:
        # If the process ended with non-zero code
        status = 1
    # dpkg -s <pkg_name> will return 0 on package being installed locally, !0 on anything else
    log_file.write('=================== END OF INSTALL CHECK FOR: {} ===================\n'.format(pkg_name.upper()))
    log_file.flush()
    return (status == 0)

# Install a package
def install_pkg(pkg_name : str) -> bool:
    # Runs the install package command and returns whether it exited with a non-zero code or not
    log_file.write('=================== INSTALL LOG FOR {} ===================\n'.format(pkg_name.upper()))
    log_file.flush()
    try:
        status = subprocess.check_call(('sudo', 'apt-get', 'install', pkg_name, '-y',), stderr=log_file,
         stdout=log_file)
    except subprocess.CalledProcessError:
        # If it exited with non 0 error
        status = 1
    log_file.write('=================== END INSTALL LOG FOR {} ===================\n'.format(pkg_name.upper()))
    log_file.flush()
    return (status == 0)


if __name__ == '__main__':
    log_file = open('setup_env.log', 'w')
    main()
    log_file.close()
    print('==============================\nScript completed successfully!\nLog file written to: setup_env.log')



"""
=========================== START NGINX SERVER CONFIGURATION ===========================

=========================== END NGINX SERVER CONFIGURATION ===========================
"""