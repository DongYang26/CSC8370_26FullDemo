### Level 3 Code Structure Requirement (For Demo Day Testing)
import torch

def generate_malicious_update(client_model_state_dict, local_dataset, device):
    """
    Args:
        client_model_state_dict (dict): A copy of the current global model's state_dict().
        local_dataset (Dataset): The local dataset assigned to this client.
        device (torch.device): CPU or CUDA device.
    Returns:
        malicious_state_dict (dict): The modified model parameters (state_dict) to be uploaded to the server.
    """
    # === STUDENTS: IMPLEMENT YOUR SIMULATED ATTACK BELOW ===
    malicious_state_dict = {}
    for key, param in client_model_state_dict.items():
        # Example: adding large Gaussian noise
        malicious_state_dict[key] = param + torch.randn_like(param) * 10.0
        
    return malicious_state_dict