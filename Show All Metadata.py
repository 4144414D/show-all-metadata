# Menu Title: Show All Metadata
# Menu Keyboard Shortcut: ctrl alt A
# Needs Selected Items: true
# Needs Case: true

# https://github.com/4144414D/show-all-metadata
print "Starting show all metadata.py script"
items = current_selected_items
metadata = set()
guids = set()
for item in items:
    guids.add(item.getGuid())
    for item_property in item.getProperties(): metadata.add(item_property)
search = "guid:("
for guid in guids: search = search + guid + " OR "
search = search[:-4] + ")"
profile = utilities.getMetadataProfileStore().createMetadataProfile()
for item in metadata: profile = profile.addMetadata("PROPERTY",item)
window.openTab("workbench",{'metadataProfile':profile,'search':search})
print "Finished show all metadata.py script"