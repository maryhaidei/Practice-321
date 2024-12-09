import math
import sys

class AssemblerInterpreter:
    def __init__(self, program):
        self.program_lines = program.splitlines()
        self.labels = {}
        self.variables = {}
        self.instructions = []
        self._parse_program()

    def _parse_program(self):
        for index, line in enumerate(self.program_lines):
            line = line.strip()
            if not line:
                continue

            if ':' in line:
                label, *rest = line.split(':', 1)
                self.labels[label.strip()] = len(self.instructions)
                line = rest[0].strip() if rest else ''
            
            if line:
                self.instructions.append(line)

    def run(self):
        pc = 0

        while pc < len(self.instructions):
            line = self.instructions[pc]
            parts = line.split()
            command, args = parts[0], parts[1:]

            if command == "stop":
                break

            if hasattr(self, f"_cmd_{command}"):
                handler = getattr(self, f"_cmd_{command}")
                pc = handler(args, pc)
            else:
                pc += 1

    def _cmd_store(self, args, pc):
        if len(args) == 2:
            try:
                self.variables[args[1]] = float(args[0])
            except ValueError:
                self.variables[args[1]] = 0.0
        return pc + 1

    def _cmd_add(self, args, pc):
        return self._arithmetic_operation(args, pc, lambda x, y: x + y)

    def _cmd_sub(self, args, pc):
        return self._arithmetic_operation(args, pc, lambda x, y: x - y)

    def _cmd_mul(self, args, pc):
        return self._arithmetic_operation(args, pc, lambda x, y: x * y)

    def _cmd_div(self, args, pc):
        return self._arithmetic_operation(args, pc, lambda x, y: x / y if y != 0 else math.inf)

    def _arithmetic_operation(self, args, pc, operation):
        if len(args) == 3:
            src = self.variables.get(args[0], 0.0)
            opn = self.variables.get(args[1], 0.0)
            self.variables[args[2]] = operation(src, opn)
        return pc + 1

    def _cmd_ifeq(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x == y)

    def _cmd_ifne(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x != y)

    def _cmd_ifgt(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x > y)

    def _cmd_ifge(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x >= y)

    def _cmd_iflt(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x < y)

    def _cmd_ifle(self, args, pc):
        return self._conditional_jump(args, pc, lambda x, y: x <= y)

    def _conditional_jump(self, args, pc, condition):
        if len(args) == 3:
            src = self.variables.get(args[0], 0.0)
            opn = self.variables.get(args[1], 0.0)
            label = args[2]
            if label in self.labels and condition(src, opn):
                return self.labels[label]
        return pc + 1

    def _cmd_out(self, args, pc):
        if len(args) == 1:
            print(self.variables.get(args[0], 0.0))
        return pc + 1


program = sys.stdin.read()
interpreter = AssemblerInterpreter(program)
interpreter.run()