from scholarly import scholarly

def fetch_google_scholar(kol_name, output_file="kol_details.txt"):
    # Search for the author by name using scholarly
    search_query = scholarly.search_author(kol_name)
    author = next(search_query, None)  # Get the first result (if exists)
    
    if author:
        # Fetch full details of the author
        author_details = scholarly.fill(author)
        
        # Write the details to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(author_details))  # Write author details as string
        print(f"Author details saved to {output_file}")
    else:
        print("Error: Author not found")

# Example usage:
fetch_google_scholar("Jitendra Kumar Singh")
