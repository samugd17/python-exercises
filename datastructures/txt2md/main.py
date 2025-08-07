def run(input_path: str, output_path: str) -> None:
    # TODO

    tab = '\t'
    lines = []
    with open(input_path, 'r') as f:
        for line in f:
            num_tabs = line.count(tab) + 1
            md_line = f'{"#" * num_tabs} {line.strip()}'
            lines.append(md_line + '\n')

    with open(output_path, 'w') as f:
        f.writelines(lines)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    run('data/animals.input.txt', 'data/animals.output.md')
    import vendor

    vendor.launch(run)
