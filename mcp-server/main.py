from mcp.server.fastmcp import FastMCP
import os
#Create a MCP server
mcp = FastMCP("AI Sticky Notes")

notes_file = os.path.join(os.path.dirname(__file__), "notes.txt")

# Check if the notes file exists
def ensure_file():
    if not os.path.exists(notes_file):
        with open(notes_file, 'w') as f:
            f.write("")
            
            
@mcp.tool()
def add_note(message: str) -> str:
    """
    Add a note to the sticky notes file.
    
    Args:
        message (str): the note content to be saved
    Returns: 
        str: Confirmation message indicating hte note was saved
        
    """ 
    ensure_file()
    with open(notes_file, 'a') as f:
        f.write(message + "\n")
    return " Note saved!"



@mcp.tool()
def read_notes() -> str:
    
    """
    Read the sticky notes file and return its content.
    
    Returns:
        str: The content of the sticky notes file.
    """
    ensure_file()
    with open(notes_file," r") as f:
        content = f.read().strip()
        return content or " No Notes found"


@mcp.resource(" notes://latest")

def get_notes() -> str:
    """
    Get the latest note from the sticky notes file. 
    Returns:
        str: The latest note from the sticky notes file.
    """
    ensure_file()
    with open(notes_file, "r") as f:
        lines = f.readlines()
        return lines[-1].strip() if lines else "No notes found"
    
@mcp.prompt()
def note_summary() -> str:
    """
    Summarize the sticky notes.
    
    Returns:
        str: The summary of the sticky notes.
    """
    ensure_file()
    with open(notes_file,"r") as f:
        content = f.read().strip()
    if not content:
            return " No Notes found"
    return f" Summarize the current notes: {content}"