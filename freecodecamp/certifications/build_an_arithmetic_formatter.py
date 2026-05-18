def arithmetic_arranger(problems, show_answers=False):
    # 1. Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists to hold each row's components
    first_lines = []
    second_lines = []
    dash_lines = []
    answer_lines = []
    
    for problem in problems:
        # Split each problem into its component parts
        parts = problem.split()
        first_num = parts[0]
        operator = parts[1]
        second_num = parts[2]
        
        # 2. Check for invalid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # 3. Check if operands contain only digits
        if not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'
            
        # 4. Check if operands are too long (max 4 digits)
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
        # --- Computation and Formatting ---
        # Determine the total width of this specific problem block
        # The width is the length of the longest number + 2 spaces (for the operator and the space after it)
        longest_val = max(len(first_num), len(second_num))
        length = longest_val + 2
        
        # Format the top line, bottom line, and dash line dynamically right-aligned
        top_row = first_num.rjust(length)
        bottom_row = operator + second_num.rjust(length - 1)
        dashes = "-" * length
        
        # Append the formatted components to their respective row lists
        first_lines.append(top_row)
        second_lines.append(bottom_row)
        dash_lines.append(dashes)
        
        # If answers are requested, compute and format them to match the column width
        if show_answers:
            num1 = int(first_num)
            num2 = int(second_num)
            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            answer_lines.append(str(result).rjust(length))
            
    # Combine individual problem columns into unified horizontal strings separated by 4 spaces
    arranged_problems = (
        "    ".join(first_lines) + "\n" +
        "    ".join(second_lines) + "\n" +
        "    ".join(dash_lines)
    )
    
    # If the second argument is True, append the answer row to the final layout
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_lines)
        
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"])}')