first_name = "Frank"
second_name = "Chen"
full_name = f'{first_name} {second_name}'
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

language = ' Original_Word '
print(f'{language},')
print(f'{language.lstrip()},')
print(f'{language.rstrip()},')
print(f'{language.strip()},')


original_url = 'https://portal.frankchen.com.cn'
print(original_url)
print(original_url.removeprefix('https://p'))