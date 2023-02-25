import argparse
import shutil
from pathlib import Path
from operator import itemgetter


_LOG_FILENAME = 'result.jsonl'


def _parse_args() -> argparse.Namespace:
    """Добавление аргументов"""

    parser = argparse.ArgumentParser(description='Tool to merge test logs')

    parser.add_argument(
        'log_a_dir',
        metavar='<LOG A DIR>',
        type=str,
        help='path to dir with log_a.jsonl',
    )

    parser.add_argument(
        'log_b_dir',
        metavar='<LOG B DIR>',
        type=str,
        help='path to dir with log_b.jsonl',
    )

    parser.add_argument(
        'output_dir',
        metavar='<OUTPUT DIR>',
        type=str,
        help='path to dir with merge logs',
    )

    parser.add_argument(
        '-o', '--output',
        action='store_const',
        const=True,
        default=False,
        help='merge logs',
        dest='merge',
    )

    return parser.parse_args()


def _create_dir(dir_path: Path, *, force_write: bool = False) -> None:
    """Создание директории для результирующего файла"""

    if dir_path.exists():
        if not force_write:
            raise FileExistsError(
                f'Dir "{dir_path}" already exists. Remove it first or choose another one.')
        shutil.rmtree(dir_path)

    dir_path.mkdir(parents=True)


def _merge_files(result_log_path: Path, log_a_dir: Path, log_b_dir: Path) -> None:
    """Метод для слияния 2-х json файлов"""

    with result_log_path.open('a+') as result_file:

        with open(log_a_dir, 'r') as file_a:
            result_file.write(file_a.read())

        with open(log_b_dir, 'r') as file_b:
            result_file.write(file_b.read())

        sorted(result_file, key=itemgetter('timestamp'))


def _add_result_file(output_dir: Path, log_a_dir: Path, log_b_dir: Path) -> None:
    """Создаем и добавляем в папку итоговый файл"""

    result_log_path = output_dir.joinpath(_LOG_FILENAME)
    _merge_files(result_log_path, log_a_dir, log_b_dir)


def main() -> None:
    """Основная функция"""

    args = _parse_args()
    output_dir = Path(args.output_dir)
    _create_dir(output_dir, force_write=args.merge)
    _add_result_file(output_dir, args.log_a_dir, args.log_b_dir)


if __name__ == '__main__':
    main()
