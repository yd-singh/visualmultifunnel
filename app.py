import os
import glob
import yaml
from simulator import simulate_onboarding
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def main():
    st.title("Onboarding Funnel Simulation Dashboard")

    # Sidebar for configuration selection
    st.sidebar.title("Configuration Selection")
    config_files = glob.glob('configs/*.yaml')
    config_files.sort()
    selected_configs = st.sidebar.multiselect(
        "Select Configuration(s)", config_files, default=config_files[0:1]
    )

    customers_count = st.sidebar.number_input("Number of Customers", min_value=1, value=100)

    if st.sidebar.button("Run Simulation"):
        if not selected_configs:
            st.warning("Please select at least one configuration.")
            return

        all_results = []
        comparative_stats = []

        for config_file in selected_configs:
            # Run simulation for each selected configuration
            results_df, summary_stats = simulate_onboarding(customers_count, config_file)
            config_name = os.path.basename(config_file)
            config_name = os.path.splitext(config_name)[0]

            # Collect results and statistics
            all_results.append((config_name, results_df, summary_stats, config_file))

            # Extract key statistics for comparison
            stats = summary_stats['metrics']
            stats['Configuration'] = config_name
            comparative_stats.append(stats)

        # Display comparative results
        if len(selected_configs) == 1:
            # Single configuration selected
            config_name, results_df, summary_stats, config_file = all_results[0]
            display_single_configuration(config_name, results_df, summary_stats, config_file)
        else:
            # Multiple configurations selected
            display_comparative_results(all_results, comparative_stats, selected_configs)

def display_single_configuration(config_name, results_df, summary_stats, config_file):
    # Display summary statistics
    st.header(f"Summary Statistics for {config_name}")
    st.markdown(summary_stats['text'])

    # Display detailed module results
    st.subheader("Detailed Module Results")
    st.dataframe(results_df)

    # Generate and display visualizations
    st.subheader("Visualizations")
    generate_visualizations(results_df, config_name)

    # Display the configuration graph
    st.markdown("#### Configuration Flow")
    config_graph = create_config_graph(config_file)
    st.graphviz_chart(config_graph)

def display_comparative_results(all_results, comparative_stats, selected_configs):
    st.header("Comparative Analysis of Selected Configurations")

    # Create a DataFrame for comparative statistics
    comparison_df = pd.DataFrame(comparative_stats)
    comparison_df = comparison_df[
        ['Configuration', 'Success Rate', 'Total Cost', 'Total Time',
         'Average Cost per Customer', 'Average Time per Customer']
    ]

    # Display comparative statistics table
    st.subheader("Comparative Statistics")
    st.dataframe(comparison_df.set_index('Configuration'))

    # Generate comparative visualizations
    st.subheader("Comparative Visualizations")
    generate_comparative_visualizations(comparison_df)

    # Optionally, allow the user to view individual configuration details
    st.subheader("Individual Configuration Details")
    for i, (config_name, results_df, summary_stats, config_file) in enumerate(all_results):
        with st.expander(f"Details for {config_name}"):
            st.markdown(summary_stats['text'])
            st.dataframe(results_df)
            # Generate visualizations for each configuration
            generate_visualizations(results_df, config_name)

            # Display the configuration graph
            st.markdown("#### Configuration Flow")
            config_graph = create_config_graph(config_file)
            st.graphviz_chart(config_graph)

def generate_visualizations(results_df, config_name):
    # Sankey Diagram
    st.markdown("#### Sankey Diagram")
    fig_sankey = create_sankey_diagram(results_df, config_name)
    st.plotly_chart(fig_sankey, use_container_width=True)

    # Time Distribution
    st.markdown("#### Time Distribution Across Modules")
    fig_time = create_time_distribution_chart(results_df)
    st.pyplot(fig_time)

    # Cost Distribution
    st.markdown("#### Cost Distribution Across Modules")
    fig_cost = create_cost_distribution_chart(results_df)
    st.pyplot(fig_cost)

    # Success Distribution
    st.markdown("#### Success Distribution Across Modules")
    fig_success = create_success_distribution_chart(results_df)
    st.pyplot(fig_success)

def generate_comparative_visualizations(comparison_df):
    # Convert percentage columns to numeric if needed
    comparison_df['Success Rate'] = comparison_df['Success Rate'].astype(float)
    comparison_df['Total Cost'] = comparison_df['Total Cost'].astype(float)
    comparison_df['Total Time'] = comparison_df['Total Time'].astype(float)

    # Success Rate Comparison
    fig_success = create_comparative_bar_chart(
        comparison_df, 'Configuration', 'Success Rate', 'Success Rate (%)',
        'Success Rate Comparison'
    )
    st.pyplot(fig_success)

    # Total Cost Comparison
    fig_cost = create_comparative_bar_chart(
        comparison_df, 'Configuration', 'Total Cost', 'Total Cost (₹)',
        'Total Cost Comparison'
    )
    st.pyplot(fig_cost)

    # Total Time Comparison
    fig_time = create_comparative_bar_chart(
        comparison_df, 'Configuration', 'Total Time', 'Total Time (minutes)',
        'Total Time Comparison'
    )
    st.pyplot(fig_time)

def create_sankey_diagram(results_df, config_name):
    # Prepare nodes and labels
    modules = results_df['Module'].tolist()
    labels = ['Start'] + modules + ['Success', 'Failed']
    label_indices = {label: idx for idx, label in enumerate(labels)}

    sources = []
    targets = []
    values = []
    link_labels = []

    # Start node to first module
    sources.append(label_indices['Start'])
    targets.append(label_indices[modules[0]])
    values.append(results_df.loc[0, 'Enter Funnel'])
    link_labels.append(f"{results_df.loc[0, 'Enter Funnel']} customers")

    # Iterate over modules
    for idx, row in results_df.iterrows():
        current_module = row['Module']
        pass_count = row['Pass']
        fail_count = row['Fail']
        current_idx = label_indices[current_module]
        enter_funnel = row['Enter Funnel']

        # On success
        if pass_count > 0:
            next_module_name = row['Next Module on Success'] or 'Success'
            if next_module_name == "Success":
                target_idx = label_indices['Success']
            else:
                target_idx = label_indices.get(next_module_name, label_indices['Success'])
            sources.append(current_idx)
            targets.append(target_idx)
            values.append(pass_count)
            percentage = (pass_count / enter_funnel) * 100
            link_labels.append(f"{pass_count} ({percentage:.1f}%) passed")

        # On failure
        if fail_count > 0:
            next_module_name = row['Next Module on Failure'] or 'Failed'
            if next_module_name == "Failed":
                target_idx = label_indices['Failed']
            else:
                target_idx = label_indices.get(next_module_name, label_indices['Failed'])
            sources.append(current_idx)
            targets.append(target_idx)
            values.append(fail_count)
            percentage = (fail_count / enter_funnel) * 100
            link_labels.append(f"{fail_count} ({percentage:.1f}%) failed")

    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        arrangement = "snap",
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color="blue"
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            label=link_labels
        ))])

    fig.update_layout(title_text=f"Sankey Diagram for {config_name}", font_size=10)
    return fig

def create_time_distribution_chart(results_df):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Module', y='Total Time', data=results_df, ax=ax, order=results_df['Module'])
    ax.set_title('Time Distribution Across Modules')
    ax.set_xlabel('Module')
    ax.set_ylabel('Total Time (seconds)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def create_cost_distribution_chart(results_df):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Module', y='Total Cost', data=results_df, ax=ax, order=results_df['Module'])
    ax.set_title('Cost Distribution Across Modules')
    ax.set_xlabel('Module')
    ax.set_ylabel('Total Cost (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def create_success_distribution_chart(results_df):
    sns.set(style="whitegrid")
    success_df = results_df[['Module', 'Pass', 'Fail']].melt(id_vars='Module', var_name='Outcome', value_name='Count')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Module', y='Count', hue='Outcome', data=success_df, ax=ax, order=results_df['Module'])
    ax.set_title('Success Distribution Across Modules')
    ax.set_xlabel('Module')
    ax.set_ylabel('Number of Customers')
    plt.xticks(rotation=45)
    plt.legend(title='Outcome')
    plt.tight_layout()
    return fig

def create_comparative_bar_chart(df, x_col, y_col, y_label, title):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=x_col, y=y_col, data=df, ax=ax)
    ax.set_title(title)
    ax.set_xlabel('Configuration')
    ax.set_ylabel(y_label)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def create_config_graph(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    modules = config['modules']
    module_dict = {module['name']: module for module in modules}
    is_start_modules = [module['name'] for module in modules if module.get('is_start', False)]
    
    # Start building the DOT graph description
    graph_lines = ['digraph G {']
    graph_lines.append('rankdir=LR;')  # Left to right orientation
    graph_lines.append('node [shape=box, style=filled, color="#EEEEEE"];')
    
    # Define nodes
    for module in modules:
        node_label = module['name']
        graph_lines.append(f'"{module["name"]}" [label="{node_label}"];')
    
    # Define edges
    for module in modules:
        current_module = module['name']
        if 'next_module_on_success' in module and module['next_module_on_success']:
            next_module = module['next_module_on_success']
            if next_module != "Success":
                graph_lines.append(f'"{current_module}" -> "{next_module}" [label="Success", color="green"];')
            else:
                graph_lines.append(f'"{current_module}" -> "Success" [label="Success", color="green"];')
        if 'next_module_on_failure' in module and module['next_module_on_failure']:
            next_module = module['next_module_on_failure']
            if next_module != "Failed":
                graph_lines.append(f'"{current_module}" -> "{next_module}" [label="Failure", color="red"];')
            else:
                graph_lines.append(f'"{current_module}" -> "Failed" [label="Failure", color="red"];')
    
    # Add Success and Failed nodes if they are used
    success_used = any(module.get('next_module_on_success') == "Success" for module in modules)
    failed_used = any(
        module.get('next_module_on_failure') == "Failed"
        for module in modules
    )
    if success_used:
        graph_lines.append('"Success" [shape=doublecircle, style=filled, color="green"];')
    if failed_used:
        graph_lines.append('"Failed" [shape=doublecircle, style=filled, color="red"];')
    
    # Start node(s)
    for start_module in is_start_modules:
        graph_lines.append(f'Start -> "{start_module}";')
    graph_lines.append('Start [shape=Mdiamond];')
    
    graph_lines.append('}')
    dot_graph = '\n'.join(graph_lines)
    return dot_graph

if __name__ == "__main__":
    main()