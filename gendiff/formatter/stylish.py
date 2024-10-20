def format_stylish(diff, depth=0):
    return iter_diff(diff, depth)

def iter_diff(diff, depth):
    INDENT_SIZE = 4
    INDENT = ' '
    lines = []
    current_indent = '' * (depth)
    lines.append(f"{current_indent}{{")
    for key in sorted(diff.keys()):
        node = diff[key]
        node_type = node.get('type')
        value = node.get('value')
        nested = node.get('nested', False)

        if node_type == 'changed':
            old_value = value.get('removed')
            new_value = value.get('added')
            old_val_str = format_value(old_value, depth + 1)
            new_val_str = format_value(new_value, depth + 1)
            prefix_minus = INDENT * ((depth + 1) * INDENT_SIZE - 2) + '- '
            prefix_plus = INDENT * ((depth + 1) * INDENT_SIZE - 2) + '+ '
            lines.append(f"{prefix_minus}{key}: {old_val_str}")
            lines.append(f"{prefix_plus}{key}: {new_val_str}")
        elif node_type == 'added':
            val_str = format_value(value, depth + 1)
            prefix = INDENT * ((depth + 1) * INDENT_SIZE - 2) + '+ '
            lines.append(f"{prefix}{key}: {val_str}")
        elif node_type == 'removed':
            val_str = format_value(value, depth + 1)
            prefix = INDENT * ((depth + 1) * INDENT_SIZE - 2) + '- '
            lines.append(f"{prefix}{key}: {val_str}")
        elif node_type == 'unchanged':
            if nested:
                val_str = iter_diff(value, depth + 1)
                prefix = INDENT * ((depth + 1) * INDENT_SIZE)
                lines.append(f"{prefix}{key}: {val_str}")
            else:
                val_str = format_value(value, depth + 1)
                prefix = INDENT * ((depth + 1) * INDENT_SIZE)
                lines.append(f"{prefix}{key}: {val_str}")
    closing_indent = INDENT * (depth * INDENT_SIZE)
    lines.append(f"{closing_indent}}}")
    return '\n'.join(lines)

def format_value(value, depth):
    INDENT_SIZE = 4
    INDENT = ' '
    if isinstance(value, dict):
        if is_diff_node(value):
            return format_value(value.get('value'), depth)
        else:
            lines = []
            current_indent = '' * (depth)
            lines.append(f"{current_indent}{{")
            for key in sorted(value.keys()):
                val_str = format_value(value[key], depth + 1)
                prefix = INDENT * ((depth + 1) * INDENT_SIZE)
                lines.append(f"{prefix}{key}: {val_str}")
            closing_indent = INDENT * (depth * INDENT_SIZE)
            lines.append(f"{closing_indent}}}")
            return '\n'.join(lines)
    else:
        return stringify_value(value)

def stringify_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)

def is_diff_node(node):
    return isinstance(node, dict) and 'type' in node and 'value' in node