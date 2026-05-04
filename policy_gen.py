def generate_policy(client_name, data_type):
    # Drafts a basic Data Handling Policy
    policy_text = f"Policy for {client_name}: All {data_type} must be encrypted at rest."
    return policy_text
