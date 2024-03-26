import click

@click.command()
@click.option('--infile',  help='docbook xml file to modify')
@click.option('--outfile',  help='docbook xml file modified')
@click.option('--maxlines', default=30, help='Maximum number of lines per listing')
def break_listing(infile, outfile, maxlines):
    """Simple program that splits program listings in a docbook xml file."""
    with open(infile, 'r') as f:
        lines = f.readlines()
    
    nl = 0    
    for i,l in enumerate(lines): 
        if '<programlisting language="c">' in l:
            nl += 1
        elif '</programlisting>' in l:
            nl = 0
        else:
            nl += 1
            
        if nl == maxlines: 
            lines[i] = lines[i] + '</programlisting>'          
            lines[i+1] = '<programlisting language="c">' + lines[i+1]
            nl = 0
           
    with open(outfile, 'w') as f:
        f.writelines(lines)    

if __name__ == '__main__':
    break_listing()