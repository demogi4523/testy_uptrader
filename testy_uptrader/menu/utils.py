def iter_to_html(json_menu: iter, json_menu_name: str = None):
    def inner(json_menu: iter):
        obj = {}
        for key, item in json_menu.items():
            print(key, item)
            if '$url' in item:
                obj[item] = json_menu[item]
                continue
            if type(item) == dict:
                obj['inner'] = iter_to_html(json_menu[item])
                continue
            return f"<li><a href={obj['$url']}>{key}<ul>{obj['inner']}</ul></a></li>" if 'inner' in obj else f"<li><a href={obj['$url']}>{key}</a></li>"

    ul = f"<ul id={json_menu_name}>{inner(json_menu)}</ul>" if json_menu_name else f"<ul>{inner(json_menu)}</ul>"
    return ul

    # return """
    #  <ul>
    #     <li><span class="caret">Beverages</span>
    #         <ul class="nested">
    #         <li>Water</li>
    #         <li>Coffee</li>
    #         <li><span class="caret">Tea</span>
    #             <ul class="nested">
    #             <li>Black Tea</li>
    #             <li>White Tea</li>
    #             <li><span class="caret">Green Tea</span>
    #                 <ul class="nested">
    #                 <li>Sencha</li>
    #                 <li>Gyokuro</li>
    #                 <li>Matcha</li>
    #                 <li>Pi Lo Chun</li>
    #                 </ul>
    #             </li>
    #             </ul>
    #         </li>
    #         </ul>
    #     </li>
    # </ul> 
    # """