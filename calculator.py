
import re
import operator as op

# Supported operations mapping
_OPERATORS = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '^': op.pow,
}

class CalculatorError(Exception):
    pass

class Calculator:
    def calculate(self, expr: str) -> float:
        # 1) Empty input => 0.0
        if not expr:
            return 0.0

        # 2) Leading operator
        current_op = '+'
        if expr[0] in _OPERATORS:
            current_op = expr[0]
            expr = expr[1:]

        # 3) Delimiter header: [del1][del2]...
        delimiters = [',']  # default
        if expr.startswith('['):
            # Match all consecutive [del] at start
            header_match = re.match(r'^(\[(?:[^\]]+)\])+', expr)
            if not header_match:
                raise CalculatorError('Invalid delimiter header')
            header = header_match.group(0)
            # Extract delimiters
            delimiters = re.findall(r'\[([^\]]+)\]', header)
            expr = expr[len(header):]

        # 4) Split tokens by delimiters
        split_pattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(split_pattern, expr)
        tokens = [t for t in tokens if t]

        # 5) Validate and compute
        result = None
        numbers = []

        for t in tokens:
            if t in _OPERATORS:
                current_op = t
            elif re.fullmatch(r"\d+", t):
                num = int(t)
                if num <= 1000:
                    numbers.append((current_op, num))
            else:
                raise CalculatorError(f"Invalid token: {t}")

        if not numbers:
            raise CalculatorError('Expression must contain at least one number')

        for op_symbol, num in numbers:
            if result is None:
                result = num
            else:
                try:
                    result = _OPERATORS[op_symbol](result, num)
                except ZeroDivisionError:
                    raise CalculatorError('Division by zero')

        return result or 0.0





