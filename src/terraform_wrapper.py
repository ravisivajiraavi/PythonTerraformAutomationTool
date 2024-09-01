from python_terraform import Terraform, IsFlagged, IsNotFlagged
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def terraform_init():
    try:
        tf = Terraform()
        return_code, stdout, stderr = tf.init(capture_output=True)
        if return_code != 0:
            logging.error(f"Terraform init failed: {stderr}")
        else:
            logging.info("Terraform init successful")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
def terraform_plan():
    try:
        tf = Terraform()
        return_code, stdout, stderr = tf.plan(capture_output=True)
        if return_code != 0:
            logging.error(f"Terraform plan failed: {stderr}")
        else:
            logging.info("Terraform plan successful")
            logging.info(stdout)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
def terraform_apply(auto_approve=True):
    try:
        tf = Terraform()
        return_code, stdout, stderr = tf.apply(skip_plan=True, auto_approve=auto_approve, capture_output=True)
        if return_code != 0:
            logging.error(f"Terraform apply failed: {stderr}")
        else:
            logging.info("Terraform apply successful")
            logging.info(stdout)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
def terraform_destroy(auto_approve=True):
    try:
        tf = Terraform()
        return_code, stdout, stderr = tf.destroy(auto_approve=auto_approve, capture_output=True)
        if return_code != 0:
            logging.error(f"Terraform destroy failed: {stderr}")
        else:
            logging.info("Terraform destroy successful")
            logging.info(stdout)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
