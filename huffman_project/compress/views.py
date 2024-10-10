from django.shortcuts import render
from .huffman import huffman_compress

def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '').strip()  # Убираем пробелы в начале и конце
        if input_text:
            encoded_text, huffman_codes = huffman_compress(input_text)
            return render(request, 'home.html', {
                'encoded_text': encoded_text,
                'huffman_codes': huffman_codes,
                'input_text': input_text,
            })
    
    # При любом GET запросе (первая загрузка страницы) очищаем все данные
    return render(request, 'home.html', {
        'encoded_text': '',  # Сбрасываем предыдущие данные
        'huffman_codes': {},  # Сбрасываем коды
        'input_text': '',  # Очищаем текстовое поле
    })
