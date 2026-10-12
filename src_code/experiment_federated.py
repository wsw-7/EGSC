"""Public entry point for conventional FedAvg baseline simulations."""
import numpy as np
from environment_federated import FL


def run_exp(dataset_name, model_name, dd_type, num_peers, frac_peers, seed,
            test_batch_size, criterion, global_rounds, local_epochs, local_bs,
            local_lr, local_momentum, labels_dict, device, attackers_ratio,
            attack_type, malicious_behavior_rate, rule, class_per_peer,
            samples_per_class, rate_unbalance, alpha, source_class, target_class,
            resume=False):
    print('Starting public baseline experiment:', dataset_name, rule)
    fl_env = FL(dataset_name, model_name, dd_type, num_peers, frac_peers, seed,
                test_batch_size, criterion, global_rounds, local_epochs, local_bs,
                local_lr, local_momentum, labels_dict, device, attackers_ratio,
                class_per_peer, samples_per_class, rate_unbalance, alpha,
                source_class, max_train_samples=max_train_samples,
                max_test_samples=max_test_samples)
    result = fl_env.run_experiment(attack_type, malicious_behavior_rate,
                                   source_class, target_class, rule, resume)
    print('End of public baseline experiment.')
    return result
