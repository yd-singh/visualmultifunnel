from funnel import Funnel

def simulate_onboarding(customers_count, config_path):
    funnel = Funnel(config_path)
    results, summary_stats = funnel.run_funnel(customers_count)
    path_metrics = funnel.compute_path_metrics()
    return results, summary_stats, path_metrics
