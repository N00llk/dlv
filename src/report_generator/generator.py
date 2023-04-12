import jinja2
import os
from typing import List


from ..decoder_8b10b import SymbolInfo, SymbolCode


def generate_symbol_report(path, symbol_info_list: List[SymbolInfo]):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates/")))
    template = environment.get_template('symbol_report.html')
    context = {
        "symbols": symbol_info_list
    }
    with open(path, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        print(f"... wrote {path}")


def generate_summary_report(path, symbol_info_list: List[List[SymbolInfo]]):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates/")))
    template = environment.get_template('summary_report.html')

    total_size = 0
    for line in symbol_info_list:
        total_size += len(line)

    context = {
        "data_size": total_size
    }

    for idx, line in enumerate(symbol_info_list):
        k_symbol_count = sum(symbol.code in range(SymbolCode.First_K, SymbolCode.Last_K) for symbol in line)
        context[f"k_symbol_line_{idx}"] = (k_symbol_count if k_symbol_count > 0 else '-')
        d_symbol_count = sum(symbol.code in range(SymbolCode.First_D, SymbolCode.Last_D) for symbol in line)
        context[f"d_symbol_line_{idx}"] = (d_symbol_count if d_symbol_count > 0 else '-')
        context[f"line_{idx}_valid"] = "Да"

    for idx in range(len(symbol_info_list), 4):
        context[f"k_symbol_line_{idx}"] = '-'
        context[f"d_symbol_line_{idx}"] = '-'
        context[f"line_{idx}_valid"] = "-"

    with open(path, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        print(f"... wrote {path}")
