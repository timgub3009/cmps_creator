import os

def create_component(component_name, component_content, include_css, include_vm, imports):
    component_dir = f"./{component_name}"
    if not os.path.exists(component_dir):
        os.makedirs(component_dir)

    view_file_path = os.path.join(component_dir, f"{component_name}.jsx")

    view_template = f"""
import React from 'react'
{imports}
import {{ {component_name}Vm }} from './{component_name}Vm';
{f"import './{component_name}.css';" if include_css else ""} 

export default const {component_name} = () => {{
    const viewModel = new {component_name}ViewModel();
    return (
        <div>
            {component_content}
        </div>
    )
}}
    """

    with open(view_file_path, "w") as file:
        file.write(view_template)
    
    print(f"View {component_name}.jsx успешно создан по пути {view_file_path}")

    if include_vm:
        vm_file_path = os.path.join(component_dir, f"{component_name}Vm.jsx")

    vm_template = f"""
import React from 'react'
{imports}

export default class {component_name}Vm {{
   
}}
"""
    with open(vm_file_path, 'w') as file:
        file.write(vm_template)

    print(f"ViewModel {component_name}Vm.jsx успешно создана по пути {vm_file_path}")
    
    if include_css:
        css_file_path = os.path.join(component_dir, f"{component_name}.scss")

        css_template = f"""

"""
        
        with open(css_file_path, 'w') as file:
            file.write(css_template)

        print(f"CSS файл {component_name}.scss успешно создан по пути {css_file_path}")

def form_to_fill():
    component_name = input('Введите название для вашего компонента: ')
    imports = input('Введите импорты: ')
    component_content = input('Введите наполнение компонента: ')
    include_css = input('Добавляем css файл? Да/Нет: ').strip().lower() == 'да'
    include_vm = input('Добавляем viewModel? Да/Нет: ').strip().lower() == 'да'
    create_component(component_name, component_content, include_css, include_vm, imports)

if __name__ == '__main__':
    form_to_fill()
    