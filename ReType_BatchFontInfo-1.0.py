# ReType Batch Font Info 1.0
# Fill up non-linking font family names/styles and family metrics following Karsten LÃ¼cke's "Font Naming" 
# (Naming Scheme B, page 8) and "Font Metrics" recommendations. 
# For future consideration see also: http://unifiedfontobject.org/versions/ufo2/fontinfo.html 
# Re-Type.com


from dialogKit import *
from robofab.world import AllFonts

class EditTextTest(object):
    
    def __init__(self):
        self.w = ModalDialog((385, 440), 'ReType Batch Font Info 1.0',okCallback=self.okCallback)
  
        self.w.editText = EditText((10, 10, 180, 27), 'Write your Font Name')
        
        self.w.ascender = EditText((10, 40, 180, 27), 'Write your Ascender')
        self.w.descender = EditText((195, 40, 180, 27), 'Write your Descender')
        
        self.w.winascender = EditText((10, 70, 180, 27), 'Write your WinAscent')
        self.w.windescender = EditText((195, 70, 180, 27), 'Write your WinDescent')
        
        self.w.italicangle = EditText((10, 100, 180, 27), 'Write your Italic angle')
        self.w.year = EditText((195, 100, 180, 27), 'Write your creation year')
        
        self.w.copyright = EditText((10, 130, 180, 100), 'Paste your Copyright text')
        self.w.trademark = EditText((195, 130, 180, 100), 'Paste your Trademark text')
        self.w.notice = EditText((195, 233, 180, 87), 'Paste your Notice text')
        
        self.w.createdby = EditText((10, 233, 180, 27), 'Who created the font')
        self.w.designer = EditText((10, 263, 180, 27), 'Who the designer is')
        self.w.website = EditText((10, 293, 180, 27), 'www.designer.com')
        self.w.vendor = EditText((10, 323, 180, 27), 'www.vendor.com')
        self.w.licenseURL = EditText((195, 323, 180, 27), 'www.license.com')
        self.w.vendorID = EditText((10, 353, 180, 27), 'Write your Vendor ID')
        self.w.UPM = EditText((195, 353, 180, 27), 'Units Per Em')
        
        self.w.open()   
 
    
    def okCallback(self, sender):
				global Name, Ascender, Descender, WinAscend, WinDescend, ItalicAngle, Copyright_text, Trademark_text
				global Year, Notice, Created_by, Designer, Website, Vendor, LicenseURL, VendorID, UPM
				Name = self.w.editText.get()
				Ascender = int(self.w.ascender.get())
				Descender = int(self.w.descender.get())
				WinAscend = int( self.w.winascender.get())
				WinDescend = abs( int(self.w.windescender.get()) )
				ItalicAngle = int(self.w.italicangle.get())
				Copyright_text = self.w.copyright.get()
				Trademark_text = self.w.trademark.get()
				Year = int(self.w.year.get())
				Notice = self.w.notice.get()
				Created_by = self.w.createdby.get()
				Designer = self.w.designer.get()
				Website = self.w.website.get()
				Vendor = self.w.vendor.get()
				LicenseURL = self.w.licenseURL.get()
				VendorID = self.w.vendorID.get()
				UPM = int(self.w.UPM.get())
	
EditTextTest()

Gap =  abs( (Ascender + abs(Descender)) - (WinAscend + WinDescend) )
Width = 5 #Equal to "Medium (normal)" 
Style_Name = "Regular" #Leave always as "Regular"

for font in AllFonts():
	font.info.familyName = Name 
	font.info.ascender = Ascender
	font.info.descender = Descender
	font.info.openTypeOS2WinAscent = WinAscend
	font.info.openTypeOS2WinDescent = WinDescend
	font.info.openTypeOS2TypoAscender = Ascender
	font.info.openTypeOS2TypoDescender = Descender
	font.info.openTypeHheaAscender = WinAscend
	font.info.openTypeHheaDescender = -abs(WinDescend)
	font.info.openTypeHheaLineGap = 0
	font.info.openTypeOS2TypoLineGap = Gap
	font.info.copyright = Copyright_text
	font.info.trademark = Trademark_text
	font.info.year = Year
	font.info.openTypeNameDescription = Notice
	font.info.openTypeNameManufacturer = Created_by
	font.info.openTypeNameDesigner = Designer
	font.info.openTypeNameDesignerURL = Website
	font.info.openTypeNameManufacturerURL = Vendor
	font.info.openTypeNameLicenseURL = LicenseURL
	font.info.openTypeOS2VendorID = VendorID
	font.info.unitsPerEm = UPM 
	
	
	
	
#Rules for weight classes
for font in AllFonts():
	if font.info.postscriptWeightName == "UltraThin" or "Ultrathin":
		font.info.openTypeOS2WeightClass = 250
	if font.info.postscriptWeightName == "ExtraThin" or "Extrathin":
		font.info.openTypeOS2WeightClass = 255
	if font.info.postscriptWeightName == "Thin":
		font.info.openTypeOS2WeightClass = 260
	if font.info.postscriptWeightName == "UltraLight" or "Ultralight":
		font.info.openTypeOS2WeightClass = 270
	if font.info.postscriptWeightName == "ExtraLight" "Extralight":
		font.info.openTypeOS2WeightClass = 280
	if font.info.postscriptWeightName == "Light":
		font.info.openTypeOS2WeightClass = 300
	if font.info.postscriptWeightName == "ExtraBook" or "Extrabook":
		font.info.openTypeOS2WeightClass = 330
	if font.info.postscriptWeightName == "Book":
		font.info.openTypeOS2WeightClass = 350
	if font.info.postscriptWeightName == "Regular":
		font.info.openTypeOS2WeightClass = 400
	if font.info.postscriptWeightName == "Normal":
		font.info.openTypeOS2WeightClass = 450
	if font.info.postscriptWeightName == "Medium":
		font.info.openTypeOS2WeightClass = 500
	if font.info.postscriptWeightName == "DemiBold" or "Demibold":
		font.info.openTypeOS2WeightClass = 550
	if font.info.postscriptWeightName == "SemiBold" or "Semibold":
		font.info.openTypeOS2WeightClass = 600
	if font.info.postscriptWeightName == "Bold":
		font.info.openTypeOS2WeightClass = 700
	if font.info.postscriptWeightName == "ExtraBold" or "Extrabold":
		font.info.openTypeOS2WeightClass = 750
	if font.info.postscriptWeightName == "Heavy":
		font.info.openTypeOS2WeightClass = 800
	if font.info.postscriptWeightName == "ExtraHeavy" or "Extraheavy":
		font.info.openTypeOS2WeightClass = 850
	if font.info.postscriptWeightName == "Black":
		font.info.openTypeOS2WeightClass = 900
	if font.info.postscriptWeightName == "ExtraBlack" or "Extrablack":
		font.info.openTypeOS2WeightClass = 950
	if font.info.postscriptWeightName == "UltraBlack" or "Ultrablack":
		font.info.openTypeOS2WeightClass = 970
	if font.info.postscriptWeightName == "Fat":
		font.info.openTypeOS2WeightClass = 1000
			
			
#Write font names
for font in AllFonts():
	if font.info.styleMapStyleName != "italic":
		Weight = font.info.postscriptWeightName
		font.info.familyName = Name + " " + Weight
	
		font.info.styleName = Style_Name
		font.info.fullName = Name + " " + Weight
	
		font.info.openTypeOS2WidthClass = Width
		font.info.postscriptFontName = Name + "-" + Weight
		
		font.info.openTypeNamePreferredFamilyName = Name
		font.info.openTypeNamePreferredSubfamilyName = Weight
	
	else:
		Weight = font.info.postscriptWeightName
		font.info.familyName = Name + " " + Weight + " " + "Italic"
	
		font.info.styleName = Style_Name
		font.info.fullName = Name + " " + Weight + " " + "Italic"
	
		font.info.openTypeOS2WidthClass = Width
		font.info.postscriptFontName = Name + "-" + Weight + "Italic"
		
		font.info.openTypeNamePreferredFamilyName = Name
		font.info.openTypeNamePreferredSubfamilyName = Weight + " " + "Italic"
		
		font.info.italicAngle = ItalicAngle
		font.info.postscriptSlantAngle = abs(ItalicAngle)

		font.info.styleMapStyleName = "regular"	
		

		
print
print "Listo el pollo!"
		
font.update()


