% Предикат для вычисления суммы элементов списка
sum_list([], 0). % Базовый случай: сумма пустого списка равна 0
sum_list([H|T], Sum) :-
    sum_list(T, RestSum), % Рекурсивный вызов для хвоста списка
    Sum is H + RestSum.  % Сумма равна голове списка плюс сумма хвоста.

% Пример использования:
?- sum_list([1, 2, 3, 4, 5], Sum).
% Результат: Sum = 15