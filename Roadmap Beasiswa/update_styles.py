import os
import re

def update_html_file(file_path):
    """Update HTML file with creative styling"""
    
    # Read the original file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add creative styling
    new_content = content.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '''<script src="https://cdn.tailwindcss.com"></script>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
      
      body {
        font-family: 'Inter', sans-serif;
      }
      
      .gradient-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }
      
      .gradient-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      }
      
      .card-hover {
        transition: all 0.3s ease;
      }
      
      .card-hover:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      }
      
      .timeline-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.2);
        backdrop-filter: blur(10px);
      }
      
      .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
      }
    </style>'''
    )
    
    # Update body class
    new_content = new_content.replace(
        'class="font-sans bg-[#060910]"',
        'class="font-sans bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 min-h-screen"'
    )
    
    # Update main container
    new_content = new_content.replace(
        'class="bg-gradient-to-b from-slate-900 to bg-[#060910] text-gray-300"',
        'class="bg-gradient-to-b from-slate-900/50 to bg-[#060910]/50 text-gray-300"'
    )
    
    # Update nav
    new_content = new_content.replace(
        'class="container mx-auto px-6 py-8 text-gray-400 text-sm font-medium"',
        'class="container mx-auto px-6 py-8 text-gray-400 text-sm font-medium backdrop-blur-sm"'
    )
    
    # Update logo link
    new_content = new_content.replace(
        '<a href="/code/index.html">',
        '<a href="/code/index.html" class="card-hover">'
    )
    
    # Update navigation links
    new_content = re.sub(
        r'<a href="#" class="hover:text-white">',
        '<a href="#" class="hover:text-white transition-colors duration-200">',
        new_content
    )
    
    # Update sign up button
    new_content = new_content.replace(
        'class="bg-blue-600 rounded-full px-6 py-1 text-white"',
        'class="gradient-bg rounded-full px-6 py-2 text-white hover:shadow-lg transition-all duration-200"'
    )
    
    # Update mobile sign up button
    new_content = new_content.replace(
        'class="bg-blue-600 rounded-full px-6 py-2 text-white w-full block text-center"',
        'class="gradient-bg rounded-full px-6 py-2 text-white w-full block text-center hover:shadow-lg transition-all duration-200"'
    )
    
    # Update main title
    new_content = re.sub(
        r'<h1 class="text-4xl font-bold text-center text-white mb-4">',
        '<h1 class="text-5xl md:text-6xl font-bold gradient-text mb-6">',
        new_content
    )
    
    # Update main description
    new_content = re.sub(
        r'<p class="text-center text-lg max-w-3xl mx-auto mb-12">',
        '<p class="text-xl text-gray-300 max-w-4xl mx-auto leading-relaxed mb-12">',
        new_content
    )
    
    # Update timeline cards
    new_content = new_content.replace(
        'class="order-1 bg-slate-900 rounded-lg shadow-xl w-5/12 px-6 py-4 border border-slate-800"',
        'class="order-1 timeline-card rounded-lg shadow-xl w-5/12 px-6 py-4 card-hover"'
    )
    
    # Update timeline circles
    new_content = new_content.replace(
        'class="z-20 flex items-center order-1 bg-slate-800 shadow-xl w-8 h-8 rounded-full"',
        'class="z-20 flex items-center order-1 gradient-bg shadow-xl w-12 h-12 rounded-full card-hover"'
    )
    
    # Update timeline line
    new_content = new_content.replace(
        'class="absolute border-2-2 border-slate-700 h-full border"',
        'class="absolute border-2-2 border-purple-500 h-full border"'
    )
    
    # Update section titles
    new_content = re.sub(
        r'<h2 class="text-2xl font-bold text-white mb-4">',
        '<h2 class="text-2xl font-bold text-white mb-4 gradient-text">',
        new_content
    )
    
    # Update pros/cons cards
    new_content = new_content.replace(
        'class="bg-slate-900 p-6 rounded-lg border border-slate-800"',
        'class="feature-card p-8 rounded-2xl card-hover"'
    )
    
    # Update requirements cards
    new_content = new_content.replace(
        'class="bg-slate-900 p-6 rounded-lg border border-slate-800 mb-12"',
        'class="feature-card p-8 rounded-2xl card-hover mb-12"'
    )
    
    # Update final paragraph
    new_content = re.sub(
        r'<p class="text-center text-gray-400 max-w-3xl mx-auto mt-12">',
        '<p class="text-center text-gray-300 max-w-3xl mx-auto mt-12 text-lg">',
        new_content
    )
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated: {file_path}")

def main():
    """Update all HTML files in the pages folder"""
    pages_dir = "code/pages"
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    update_html_file(file_path)
                except Exception as e:
                    print(f"Error updating {file_path}: {e}")

if __name__ == "__main__":
    main() 