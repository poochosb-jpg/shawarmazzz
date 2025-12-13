import os

menu_categories = [
    {
        "title": "1. Entradas Árabes (Por ración)",
        "items": [
            ("Hummus (Crema de garbanzos)", "9", "Crema de garbanzos"),
            ("Tabaquitos de Uva", "9", ""),
            ("Mutabal (Crema de berenjenas)", "9", ""),
            ("Muhammara (Crema de pimentón)", "12", ""),
            ("Labne (Crema de yogurt)", "10", ""),
            ("Makanek (Salchicha árabe)", "13", ""),
            ("Basterma (Carne curada)", "12", ""),
            ("Sawda Djaj (Hígado de pollo)", "12", ""),
            ("Cremas mixtas", "12", ""),
            ("Garbanzo con lomito", "14", ""),
            ("Kibbe crudo", "13", ""),
            ("Kibbe frito", "13", ""),
            ("Kibbe horneado", "13", ""),
            ("Falafel", "7", ""),
            ("Tabaquitos mixtos", "12", ""),
            ("Tabaquitos de Repollo", "12", "")
        ]
    },
    {
        "title": "2. Entradas Mediterráneas",
        "items": [
            ("Carpaccio de Lomito", "17", ""),
            ("Ceviche de camarón", "16", ""),
            ("Berenjena frita", "11", ""),
            ("Dedos de mozzarella", "9", ""),
            ("Tequeños (8 unidades)", "8", ""),
            ("Papas fritas", "6", "")
        ]
    },
    {
        "title": "3. Sopas y Cremas",
        "items": [
            ("Fosforera", "16", ""),
            ("Sopa de pollo con vegetales", "12", ""),
            ("Crema de pollo", "11", "Veluté cremosa del chef"),
            ("Crema de Auyama", "11", "")
        ]
    },
    {
        "title": "4. Ensaladas",
        "items": [
            ("Ensalada de Burrata", "17", ""),
            ("Tabbule", "11", ""),
            ("Fattoush", "14", ""),
            ("Yogurt con pepino", "12", ""),
            ("Libanesa", "13", ""),
            ("Armenia", "11", ""),
            ("Ensalada César con pollo", "17", ""),
            ("Ensalada César con camarón", "19", ""),
            ("Ensalada de Palmitos", "10", ""),
            ("Ensalada mixta", "8", ""),
            ("Ensalada de camarones", "18", "")
        ]
    },
    {
        "title": "5. Platos Árabes Especiales",
        "items": [
            ("Fatte", "14", ""),
            ("Fatte de berenjena", "14", ""),
            ("Kibbe al yogurt (5 unidades)", "18", ""),
            ("Plato mixto", "20", ""),
            ("Plato mixto con lomito", "22", ""),
            ("Arroz libanés con pollo o cordero", "20", ""),
            ("Plato vegetariano árabe", "18", ""),
            ("Plato de shawarma", "34", ""),
            ("Bandeja Árabe (2 PERSONAS)", "45", ""),
            ("Bandeja árabe (3 personas)", "65", ""),
            ("Bandeja árabe (4 personas)", "75", "")
        ]
    },
    {
        "title": "6. Shawarmas",
        "items": [
            ("Shawarma", "8", "Proteína a elegir con vegetales"),
            ("Sandwich de falafel", "8", ""),
            ("Shawarma especial", "10", ""),
            ("Shawarma súper especial", "11", "")
        ]
    },
    {
        "title": "7. Sandwiches (Acompañados con papas fritas)",
        "items": [
            ("Fajita", "13", ""),
            ("Philadelphia", "13", ""),
            ("Tawook (Pollo a la brasa)", "13", ""),
            ("Camarón", "13", ""),
            ("Lomito", "13", ""),
            ("Kebab", "13", ""),
            ("Makanek (Salchicha árabe)", "13", ""),
            ("Hígado de pollo", "13", "")
        ]
    },
    {
        "title": "8. Parrillas",
        "items": [
            ("Parrilla El Amir", "60", ""),
            ("Parrilla mar y tierra", "25", ""),
            ("Parrilla de mariscos", "24", ""),
            ("Parrilla de pollo", "19", ""),
            ("Parrilla de lomito", "23", ""),
            ("Parrilla mixta", "23", ""),
            ("Brocheta de kafta", "19", ""),
            ("Brocheta de pollo", "19", ""),
            ("Brocheta de lomito", "22", ""),
            ("Brocheta mixta", "22", ""),
            ("Brochetas El Amir", "60", "")
        ]
    },
    {
        "title": "9. Carnes y Aves (Acompañados con 2 contornos)",
        "items": [
            ("Filet mignon", "22", ""),
            ("Cordon Bleu de lomito", "22", ""),
            ("Cordon Bleu de pollo", "22", ""),
            ("Centro de lomito a la plancha (300 g)", "20", ""),
            ("Pollo al champiñón", "20", ""),
            ("Pollo a la milanesa", "18", ""),
            ("Pollo a la plancha (300 gramos)", "16", ""),
            ("Mongolian beef", "18", ""),
            ("Mongolian chicken", "18", ""),
            ("Pollo a la brasa (300 gramos)", "16", ""),
            ("Pollo a la canasta", "16", ""),
            ("Tenders de pollo crispy", "16", ""),
            ("Suprema de pollo crispy", "23", ""),
            ("Envoltini de pollo con salsa de ajoporro", "19", "")
        ]
    },
    {
        "title": "10. Contornos",
        "items": [
            ("Papas fritas", "", ""),
            ("Papas bravas", "", ""),
            ("Papas rústicas", "", ""),
            ("Puré de papas", "", ""),
            ("Vegetales al vapor", "", ""),
            ("Ensalada mixta", "", ""),
            ("Arroz", "", "")
        ]
    },
    {
        "title": "11. Pescados y Mariscos",
        "items": [
            ("Mero en 2 salsas amatriciana y alcaparras", "23", ""),
            ("Mero a la plancha", "22", ""),
            ("Mero al ajillo", "23", ""),
            ("Arroz a la marinera", "45", ""),
            ("Cazuela de mariscos", "17", ""),
            ("Pulpo al grill", "22", ""),
            ("Dynamite shrimp (coctel de camarones)", "20", ""),
            ("Asopado de mariscos (2 personas)", "45", ""),
            ("Paella (2 personas)", "45", ""),
            ("Camarones a la plancha", "18", "Con dos contornos"),
            ("Camarones al ajillo", "18", "Con dos contornos"),
            ("Camarones rebozados", "18", "Con dos contornos"),
            ("Calamares al ajillo", "19", "Con dos contornos"),
            ("Calamares rebozados", "19", "Con dos contornos"),
            ("Langostinos", "23", "Con dos contornos")
        ]
    },
    {
        "title": "12. Arroces",
        "items": [
            ("Risotto al pesto con escalopines de pollo", "18", ""),
            ("Risotto con calabaza y calamares acevichados", "18", "")
        ]
    },
    {
        "title": "13. Pastas",
        "items": [
            ("Fetuccine con Ragú de Mero", "21", ""),
            ("Linguini con camarones", "19", ""),
            ("Linguini al Fileto", "18", ""),
            ("Linguini Marinera", "18", ""),
            ("Linguini Carbonara", "17", ""),
            ("Pasta Bologna", "12", ""),
            ("Pasta Napoli", "12", ""),
            ("Pasticho tradicional", "12", ""),
            ("Spaghetti con salchicha italiana a la paella (2 personas)", "30", ""),
            ("Cartoccio de lomito", "22", ""),
            ("Rigatoni cremoso con tocineta y champiñones", "20", "")
        ]
    },
    {
        "title": "14. Hamburguesas (Acompañadas por papas fritas)",
        "items": [
            ("Cheeseburger", "13", ""),
            ("Pollo Crispy", "13", ""),
            ("Oh My Burger!", "13", "")
        ]
    },
    {
        "title": "15. Bebidas y Licores",
        "items": [
            ("Batidos", "3.5", "Mora, Fresa, Melón, Piña, Melocotón, Guanábana, Lechosa, Parchita, Limonada"),
            ("Yogurt con hierbabuena", "6", ""),
            ("Yogurt con frutas", "6", ""),
            ("Merengada de frutas", "6", ""),
            ("Agua mineral", "1.50", ""),
            ("Nestea", "2", ""),
            ("Té Lipton", "3", ""),
            ("Gatorade", "3", ""),
            ("Jarra de Nestea (x4)", "10", ""),
            ("Refresco de lata", "2", ""),
            ("Refresco 1L", "3", ""),
            ("Refresco 1.5L", "4", ""),
            ("Soda/Sparkling", "2", ""),
            ("Trago de whisky (8 años)", "6", ""),
            ("Trago de whisky (12 años)", "7", ""),
            ("Trago de whisky (18 años)", "10", ""),
            ("Copa de Vino", "5", ""),
            ("Trago de anís", "4", ""),
            ("Cocteles", "6", "Cuba Libre, Margarita, Daiquiri, Mojito, Piña Colada..."),
            ("Cerveza importada", "4", ""),
            ("Cerveza nacional", "1.5", ""),
            ("Arguile", "12", "")
        ]
    }
]

html_output = '<!-- MENU MODAL (Generated) -->\n<div id="menuModal" class="menu-modal">\n    <div class="menu-modal-content">\n'
html_output += '        <div class="menu-modal-header">\n'
html_output += '            <h2>Menú Completo</h2>\n'
html_output += '            <span class="close-menu" onclick="closeMenu()">&times;</span>\n'
html_output += '        </div>\n'

html_output += '        <!-- Menu Section inside Modal -->\n'
html_output += '        <section id="menu" class="menu-section">\n'

# Generate Navigation
html_output += '            <div class="menu-nav-container">\n'
html_output += '                <div class="menu-nav">\n'
for i, category in enumerate(menu_categories):
    active_class = " active" if i == 0 else ""
    title_short = category["title"].split(".")[1].split("(")[0].strip() # Extract "Entradas Árabes" from "1. Entradas Árabes (Por ración)"
    html_output += f'                    <button class="menu-nav-btn{active_class}" onclick="filterCategory(\'cat-{i}\', this)">{title_short}</button>\n'
html_output += '                </div>\n'
html_output += '            </div>\n'

html_output += '            <div class="menu-container">\n'

for i, category in enumerate(menu_categories):
    active_class = " active-section" if i == 0 else ""
    html_output += f'            <div id="cat-{i}" class="category-section{active_class}">\n'
    html_output += f'                <h2 class="category-title">{category["title"]}</h2>\n'
    html_output += f'                <div class="product-grid">\n'
    
    for item in category["items"]:
        name = item[0]
        price = f"${item[1]}" if item[1] else ""
        desc = item[2]
        
        html_output += f'                <div class="product-card">\n'
        html_output += f'                    <div class="product-image-container">\n'
        html_output += f'                        <img src="placeholder.jpg" alt="{name}">\n'
        html_output += f'                    </div>\n'
        html_output += f'                    <div class="product-info">\n'
        html_output += f'                        <h3 class="product-title">{name}</h3>\n'
        if price:
            html_output += f'                        <div class="product-price">{price}</div>\n'
        if desc:
            html_output += f'                        <p class="product-description">{desc}</p>\n'
        else:
             html_output += f'                        <p class="product-description"></p>\n'
             
        html_output += f'                        <div class="product-actions">\n'
        html_output += f'                            <a href="https://wa.link/n5ny82" target="_blank" class="btn-add">Ordenar</a>\n'
        html_output += f'                        </div>\n'
        html_output += f'                    </div>\n'
        html_output += f'                </div>\n'
    
    html_output += '                </div>\n' # Close product-grid
    html_output += '            </div>\n'     # Close category-section
        


html_output += '''
    <script>
        function openMenu() {
            document.getElementById('menuModal').style.display = 'block';
            document.body.style.overflow = 'hidden';
        }

        function closeMenu() {
            document.getElementById('menuModal').style.display = 'none';
            document.body.style.overflow = 'auto';
        }

        // Close modal when clicking outside (on the overlay)
        window.onclick = function (event) {
            const modal = document.getElementById('menuModal');
            if (event.target == modal) {
                closeMenu();
            }
        }

        function filterCategory(categoryId, btn) {
            // Hide all sections
            const sections = document.querySelectorAll('.category-section');
            sections.forEach(sec => sec.classList.remove('active-section'));
            
            // Show selected
            document.getElementById(categoryId).classList.add('active-section');
            
            // Update buttons
            const buttons = document.querySelectorAll('.menu-nav-btn');
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Smooth scroll to top of menu container
             const container = document.querySelector('.menu-modal');
             container.scrollTo({ top: 0, behavior: 'smooth' });
        }
    </script>
'''

html_output += '            </div>\n        </section>\n    </div>\n</div>\n'

# Read original
with open(r'c:\Users\abrasha\Downloads\SHAWARMAS_KING\shawarmazzz\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Split (Handle both cases or current case)
# Split Logic Updated
if '<!-- MENU MODAL (Generated) -->' in content:
    part1 = content.split('<!-- MENU MODAL (Generated) -->')[0]
elif '<!-- MENU SECTION (Generated) -->' in content:
    part1 = content.split('<!-- MENU SECTION (Generated) -->')[0]
else:
    part1 = content.split('<!-- FAMOUS DISHES SECTION -->')[0]

part2_start_index = content.find('<!-- LOCATION SECTION -->')

# Check if part2_start_index is before the end of part1, which implies duplication or confusion
# But finding LOCATION SECTION is robust as long as it exists.
# The issue earlier was that part1 included the whole file because the split failed.

part2 = content[part2_start_index:]

# Clean up part2: it might contain the previously appended Menu Modal if we are not careful
if '<!-- MENU MODAL (Generated) -->' in part2:
     part2 = part2.split('<!-- MENU MODAL (Generated) -->')[0]
     # Fix closing tags if we cut it off
     if '</body>' not in part2:
         part2 += "</body>\n</html>"
elif '<!-- MENU MODAL -->' in part2: # Old marker check just in case
    part2 = part2.split('<!-- MENU MODAL -->')[0]
    part2 += "</body>\n</html>"

# Conversions for Info Updates
# Hours Update
part1 = part1.replace("11 AM a 11 PM", "12:00 PM a 12:00 AM")
part1 = part1.replace("⏰ Abierto todos los días de 11 AM a 11 PM", "⏰Todos los días 12:00 PM a 12:00 AM")
part1 = part1.replace("⏰ Abierto todos los días de 12:00 PM a 12:00 AM", "⏰Todos los días 12:00 PM a 12:00 AM") # Safe check

# Description Update
part1 = part1.replace("🇱🇧 Comida árabe e internacional 🇱🇧", "Gastronomía Árabe/Libanesa e Internacional 🌯")

# Location Title Removal
part2 = part2.replace('<h2 class="section-title">Nuestra Ubicación</h2>', '')

# Phone: +58 424-8738114 -> +58 424-8060218
part1 = part1.replace("+58 424-8738114", "+58 424-8060218")
part2 = part2.replace("+58 424-8738114", "+58 424-8060218")

# Address Update
old_address = """Centro Comercial Forum Plaza<br>Locales 13 y 14, Lechería<br>Estado
                    Anzoátegui, Venezuela"""
new_address = "Nuevo Local El Amir Palace<br>Detrás del viejo local"
part2 = part2.replace(old_address, new_address)

new_content = part1 + html_output + part2

with open(r'c:\Users\abrasha\Downloads\SHAWARMAS_KING\shawarmazzz\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Menu update complete.")
