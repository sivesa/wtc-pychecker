from pycodestylecopy import *
import re

def wtc_banner():
    print("""
██╗    ██╗████████╗ ██████╗         ██████╗ ██╗   ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║╚══██╔══╝██╔════╝         ██╔══██╗╚██╗ ██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║   ██║   ██║      █████╗  ██████╔╝ ╚████╔╝ ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║   ██║   ██║      ╚════╝  ██╔═══╝   ╚██╔╝  ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝   ██║   ╚██████╗         ██║        ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝    ╚═╝    ╚═════╝         ╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                     
    """)


def snakecasing(string):
    """
    Checks if function def string is a snake case.
    """
    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return lowercase(string[0]) + re.sub(r"[A-Z]", lambda matched: '_' + lowercase(matched.group(0)), string[1:])

def _main():
    """Parse options and run checks on Python source."""
    import signal

    # Handle "Broken pipe" gracefully
    try:
        signal.signal(signal.SIGPIPE, lambda signum, frame: sys.exit(1))
    except AttributeError:
        pass    # not supported on Windows

    style_guide = StyleGuide(parse_argv=True)
    options = style_guide.options

    if options.doctest or options.testsuite:
        from testsuite.support import run_tests
        report = run_tests(style_guide)
    else:
        report = style_guide.check_files()

    if options.statistics:
        report.print_statistics()

    if options.benchmark:
        report.print_benchmark()

    if options.testsuite and not options.quiet:
        report.print_results()

    if report.total_errors:
        if options.count:
            sys.stderr.write(str(report.total_errors) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    _main()