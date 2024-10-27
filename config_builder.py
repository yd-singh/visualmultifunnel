import streamlit as st
import yaml

def main():
    st.title("Funnel Configuration Builder")

    # Initialize session state
    if 'funnel_name' not in st.session_state:
        st.session_state.funnel_name = ''
    if 'modules' not in st.session_state:
        st.session_state.modules = {}
    if 'module_ids' not in st.session_state:
        st.session_state.module_ids = []
    if 'module_counter' not in st.session_state:
        st.session_state.module_counter = 0

    # Step 1: Get Funnel Name
    if not st.session_state.funnel_name:
        st.header("Step 1: Enter Funnel Name")
        with st.form(key='funnel_name_form'):
            funnel_name_input = st.text_input("Funnel Name")
            submit_funnel_name = st.form_submit_button(label='Set Funnel Name')
        if submit_funnel_name:
            if funnel_name_input.strip() == '':
                st.error("Funnel name cannot be empty.")
            else:
                st.session_state.funnel_name = funnel_name_input.strip().replace(' ', '_')
                st.success(f"Funnel name set to '{st.session_state.funnel_name}'")
    else:
        st.header(f"Building Funnel: {st.session_state.funnel_name}")

        # Button to add a new module
        if st.button("Add Module ➕"):
            st.session_state.module_counter += 1
            module_id = f"module_{st.session_state.module_counter}"
            st.session_state.module_ids.append(module_id)
            st.session_state.modules[module_id] = {
                'name': '',
                'is_start': False,
                'success_rate': 0.9,
                'cost_per_transaction': 1.0,
                'time_to_complete': 30,
                'next_module_on_success': '',
                'next_module_on_failure': '',
            }

        # Display existing modules
        if st.session_state.modules:
            st.subheader("Modules")
            modules_to_delete = []
            for module_id in st.session_state.module_ids:
                module = st.session_state.modules[module_id]
                if not display_module_form(module_id, module):
                    modules_to_delete.append(module_id)

            # Delete modules marked for deletion
            if modules_to_delete:
                for module_id in modules_to_delete:
                    delete_module(module_id)

        # Display YAML and visualization if at least one module is defined
        if any(module['name'] != '' for module in st.session_state.modules.values()):
            # Display YAML configuration
            st.subheader("YAML Configuration")
            config_data = {'modules': list(st.session_state.modules.values())}
            yaml_str = yaml.dump(config_data, sort_keys=False)
            st.code(yaml_str, language='yaml')

            # Display funnel visualization
            st.subheader("Funnel Visualization")
            config_graph = create_config_graph(st.session_state.modules)
            st.graphviz_chart(config_graph)

            # Option to download YAML file
            st.subheader("Download Configuration")
            yaml_bytes = yaml_str.encode('utf-8')
            st.download_button(
                label="Download YAML",
                data=yaml_bytes,
                file_name=f"{st.session_state.funnel_name}.yaml",
                mime='text/plain'
            )

        # Option to reset
        if st.button("Reset and Start Over"):
            reset_state()

def display_module_form(module_id, module):
    expanded = True if module['name'] == '' else False
    with st.expander(f"Module: {module.get('name', 'New Module')}", expanded=expanded):
        with st.form(key=f"form_{module_id}"):
            # Module Name
            name_input = st.text_input("Module Name", value=module['name'])
            # Standardize module name
            name = name_input.strip().upper().replace(' ', '_')
            # Ensure the module name is unique
            existing_names = [m['name'] for mid, m in st.session_state.modules.items() if mid != module_id]
            if name in existing_names and name != '':
                st.error("Module name must be unique.")
                name = ''
            module['name'] = name

            # Is Start Module
            is_start = st.checkbox("Is Start Module", value=module['is_start'])
            module['is_start'] = is_start

            # Success Rate
            success_rate = st.number_input("Success Rate (0 to 1)", min_value=0.0, max_value=1.0, value=module['success_rate'])
            module['success_rate'] = success_rate

            # Cost per Transaction
            cost_per_transaction = st.number_input("Cost per Transaction (₹)", min_value=0.0, value=module['cost_per_transaction'])
            module['cost_per_transaction'] = cost_per_transaction

            # Time to Complete
            time_to_complete = st.number_input("Time to Complete (seconds)", min_value=0, value=module['time_to_complete'])
            module['time_to_complete'] = time_to_complete

            # Next Module on Success
            next_module_on_success_input = st.text_input(
                "Next Module on Success",
                value=module['next_module_on_success'],
                help="Enter module name or 'APPROVED'/'REJECTED' for terminal steps."
            )
            next_module_on_success = next_module_on_success_input.strip().upper().replace(' ', '_')
            module['next_module_on_success'] = next_module_on_success

            # Next Module on Failure
            next_module_on_failure_input = st.text_input(
                "Next Module on Failure",
                value=module['next_module_on_failure'],
                help="Enter module name or 'APPROVED'/'REJECTED' for terminal steps."
            )
            next_module_on_failure = next_module_on_failure_input.strip().upper().replace(' ', '_')
            module['next_module_on_failure'] = next_module_on_failure

            # Submit and Delete buttons
            col1, col2 = st.columns(2)
            with col1:
                submit = st.form_submit_button("Save Module")
            with col2:
                delete = st.form_submit_button("Delete Module")

            if submit:
                # Handle new modules specified in next modules
                for next_module_name in [next_module_on_success, next_module_on_failure]:
                    if next_module_name and next_module_name not in ['APPROVED', 'REJECTED']:
                        # Check if the module already exists
                        existing_module_names = [m['name'] for m in st.session_state.modules.values()]
                        if next_module_name not in existing_module_names:
                            # Add new module
                            st.session_state.module_counter += 1
                            new_module_id = f"module_{st.session_state.module_counter}"
                            st.session_state.module_ids.append(new_module_id)
                            st.session_state.modules[new_module_id] = {
                                'name': next_module_name,
                                'is_start': False,
                                'success_rate': 0.9,
                                'cost_per_transaction': 1.0,
                                'time_to_complete': 30,
                                'next_module_on_success': '',
                                'next_module_on_failure': '',
                            }
                st.success(f"Module '{module['name']}' saved.")
                return True  # Return True to indicate the module is not deleted

            if delete:
                return False  # Return False to indicate the module should be deleted

            return True  # If neither submit nor delete was pressed

def delete_module(module_id):
    module_name = st.session_state.modules[module_id]['name']
    del st.session_state.modules[module_id]
    st.session_state.module_ids.remove(module_id)
    st.success(f"Module '{module_name}' deleted.")

    # Remove references to the deleted module in other modules
    for mod in st.session_state.modules.values():
        if mod['next_module_on_success'] == module_name:
            mod['next_module_on_success'] = ''
        if mod['next_module_on_failure'] == module_name:
            mod['next_module_on_failure'] = ''

def create_config_graph(modules_dict):
    modules = modules_dict.values()
    graph_lines = ['digraph G {']
    graph_lines.append('rankdir=LR;')  # Left to right orientation
    graph_lines.append('node [shape=box, style=filled, color="#EEEEEE"];')

    # Define nodes
    for module in modules:
        if module['name'] != '':
            node_label = module['name']
            graph_lines.append(f'"{module["name"]}" [label="{node_label}"];')

    # Define edges
    for module in modules:
        if module['name'] != '':
            current_module = module['name']
            next_success = module['next_module_on_success']
            next_failure = module['next_module_on_failure']

            if next_success:
                graph_lines.append(f'"{current_module}" -> "{next_success}" [label="Success", color="green"];')
            if next_failure:
                graph_lines.append(f'"{current_module}" -> "{next_failure}" [label="Failure", color="red"];')

    # Add APPROVED and REJECTED nodes if they are used
    approved_used = any(
        m['next_module_on_success'] == 'APPROVED' or m['next_module_on_failure'] == 'APPROVED'
        for m in modules if m['name'] != ''
    )
    rejected_used = any(
        m['next_module_on_success'] == 'REJECTED' or m['next_module_on_failure'] == 'REJECTED'
        for m in modules if m['name'] != ''
    )
    if approved_used:
        graph_lines.append('"APPROVED" [shape=doublecircle, style=filled, color="green"];')
    if rejected_used:
        graph_lines.append('"REJECTED" [shape=doublecircle, style=filled, color="red"];')

    # Start node to the start modules
    start_modules = [module['name'] for module in modules if module['is_start'] and module['name'] != '']
    if start_modules:
        graph_lines.append('Start [shape=Mdiamond];')
        for start_module in start_modules:
            graph_lines.append(f'Start -> "{start_module}";')

    graph_lines.append('}')
    dot_graph = '\n'.join(graph_lines)
    return dot_graph

def reset_state():
    st.session_state.funnel_name = ''
    st.session_state.modules = {}
    st.session_state.module_ids = []
    st.session_state.module_counter = 0

if __name__ == "__main__":
    main()