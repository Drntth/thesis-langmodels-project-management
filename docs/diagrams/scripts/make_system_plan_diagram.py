from graphviz import Digraph

dot = Digraph(format="png")

dot.node('Frontend', 'Frontend\n(HTML, CSS, JS, Bootstrap)', shape='box', style='filled', fillcolor='lightblue')
dot.node('Backend', 'Django Backend', shape='box', style='filled', fillcolor='lightgrey')

apps = {
    'ai_documentation': 'AI Documentation',
    'ai_models': 'AI Models',
    'authentication': 'Auth System',
    'home': 'Home',
    'project_management': 'Project Management',
    'users': 'User Management'
}

for key, value in apps.items():
    dot.node(key, value, shape='ellipse', style='filled', fillcolor='lightyellow')
    dot.edge('Backend', key)

dot.edge('Frontend', 'Backend', label='API Calls (REST)')

dot.node('Database', 'SQLite Database', shape='cylinder', style='filled', fillcolor='lightgreen')
dot.edge('Backend', 'Database', label='Django ORM')

dot.node('HuggingFace', 'Hugging Face API\n(Transformers, Pipeline)', shape='parallelogram', style='filled', fillcolor='orange')
dot.edge('Backend', 'HuggingFace', label='API Requests')

dot.node('Docker', 'Docker\nContainerized Deployment', shape='box3d', style='filled', fillcolor='lightcoral')
dot.edge('Docker', 'Backend')

dot.render('system_architecture', view=True)