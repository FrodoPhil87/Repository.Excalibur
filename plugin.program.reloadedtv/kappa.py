import xbmc
import xbmcgui
import threading
import os
import base64 as o0o1oi1i10i1i1
import xbmcaddon
import random
if 64 - 64: i11iIiiIii
OO0o = 'plugin.program.reloadedtv'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = Oo0Ooo . getAddonInfo ( 'path' )
iiiii = os . path . join ( O0O0OO0O0O0 , 'resources' )
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( title, result ) :
 i1I11i = [ ]
 OoOoOO00 = - 1
 I11i = None
 O0O = [ 'palegreen' , 'skyblue' ]
 for id , Oo , I1ii11iIi11i in result :
  try :
   if id == I1IiI ( 'a29kaS1mYXZvdXJpdGU=' ) :
    o0OOO = os . path . join ( iiiii , I1IiI ( 'cG5n' ) , I1IiI ( 'ZmF2b3VyaXRlLnBuZw==' ) )
    iIiiiI = ''
   elif id == I1IiI ( 'aXB0di1wbGF5bGlzdA==' ) :
    o0OOO = os . path . join ( iiiii , I1IiI ( 'cG5n' ) , I1IiI ( 'cGxheWxpc3QucG5n' ) )
    iIiiiI = ''
   elif id == I1IiI ( 'cHZyLmlwdHZzaW1wbGU=' ) :
    o0OOO = os . path . join ( iiiii , I1IiI ( 'cG5n' ) , I1IiI ( 'cHZyLnBuZw==' ) )
    iIiiiI = ''
   elif id == I1IiI ( 'cGx1Z2luLnByb2dyYW0ubXR2Z3VpZGVwcm8=' ) :
    o0OOO = os . path . join ( iiiii , I1IiI ( 'cG5n' ) , I1IiI ( 'UmVsb2FkZWQgVFYucG5n' ) )
    iIiiiI = ''
   else :
    Iii1ii1II11i = xbmcaddon . Addon ( id )
    o0OOO = Iii1ii1II11i . getAddonInfo ( I1IiI ( 'aWNvbg==' ) )
    iIiiiI = Iii1ii1II11i . getAddonInfo ( I1IiI ( 'bmFtZQ==' ) )
    if 10 - 10: I1iII1iiII + I1Ii111 / OOo
   if not iIiiiI :
    iIiiiI = Oo
   if not o0OOO :
    o0OOO = ''
    if 41 - 41: I1II1
   OoOoOO00 = OoOoOO00 + 1
   if 100 - 100: iII1iII1i1iiI % iiIIIII1i1iI % iiI11iii111 % i1I1Ii1iI1ii
  except :
   pass
  II1iI = random . choice ( O0O )
  while II1iI == I11i :
   II1iI = random . choice ( O0O )
  I11i = II1iI
  Oo = "[COLOR " + II1iI + "]" + Oo + "[/COLOR]"
  i1I11i . append ( [ Oo , OoOoOO00 , o0OOO , I1ii11iIi11i ] )
  if 27 - 27: ooo0Oo0 * i1 - OOooo0000ooo
 return OOo000 ( title , i1I11i )
 if 82 - 82: o000o0o00o0Oo . ii11 % oO0o0o0ooO0oO / I1i1I - OoOoo0 % OOooo0000ooo
def I1IiI ( KappaPride ) :
 iIiiI1 = o0o1oi1i10i1i1 . b64decode ( KappaPride )
 return iIiiI1
 if 68 - 68: OOo - i11iIiiIii - iII1iII1i1iiI / i1 - iII1iII1i1iiI + I1iII1iiII
class IiiIII111ii ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  xbmcgui . WindowXMLDialog . __init__ ( self )
  self . title = kwargs . get ( I1IiI ( 'dGl0bGU=' ) )
  self . options = kwargs . get ( I1IiI ( 'b3B0aW9ucw==' ) )
  self . icons = kwargs . get ( I1IiI ( 'aWNvbnM=' ) )
  self . selected = kwargs . get ( I1IiI ( 'c2VsZWN0ZWQ=' ) )
  self . option = - 1
  if 3 - 3: ii11 + iIIi1iI1II111
  if 42 - 42: i1 / I1iII1iiII + i11iIiiIii - o000o0o00o0Oo
 def onInit ( self ) :
  try :
   self . list = self . getControl ( 6 )
   self . getControl ( 3 ) . setVisible ( False )
  except :
   self . list = self . getControl ( 3 )
   if 78 - 78: iII1iII1i1iiI
  self . getControl ( 5 ) . setVisible ( False )
  self . getControl ( 1 ) . setLabel ( self . title )
  if 18 - 18: iIIi1iI1II111 - ii11 / ii11 + OoOoo0 % OoOoo0 - oO0o0o0ooO0oO
  for OoOoOO00 , O0O00Ooo in enumerate ( self . options ) :
   OOoooooO = xbmcgui . ListItem ( O0O00Ooo )
   OOoooooO . setIconImage ( self . icons [ OoOoOO00 ] )
   self . list . addItem ( OOoooooO )
   if 14 - 14: OOooo0000ooo % iIIi1iI1II111
  self . setFocus ( self . list )
  self . list . selectItem ( self . selected )
  if 41 - 41: I1iII1iiII + I1i1I + i1 - oO0o0o0ooO0oO
 def onFocus ( self , controlID ) :
  pass
  if 77 - 77: I1II1 . oO0o0o0ooO0oO % OoOoo0
  if 42 - 42: ooo0Oo0 - I1iII1iiII / i11iIiiIii + i1 + iII1iII1i1iiI
 def onClick ( self , controlID ) :
  if controlID in [ 7 , 99 ] :
   self . option = - 1
   return self . close ( )
   if 17 - 17: ooo0Oo0 . I1II1 . i1I1Ii1iI1ii
  if controlID == 6 or controlID == 3 :
   self . option = self . list . getSelectedPosition ( )
   self . close ( )
   if 3 - 3: iiIIIII1i1iI . I1II1 . OOo / o000o0o00o0Oo
 def onAction ( self , action ) :
  IiiiI1II1I1 = action . getId ( )
  if 95 - 95: oOooOoO0Oo0O . ii11i
  if IiiiI1II1I1 == 1 :
   self . setFocus ( self . list )
   if 67 - 67: i1 / oOooOoO0Oo0O % OOooo0000ooo - ii11i
  if IiiiI1II1I1 in ( 9 , 10 , 92 , 216 , 247 , 257 , 275 , 61467 , 61448 ) :
   self . option = - 1
   self . close ( )
   if 82 - 82: i11iIiiIii . i1 / I1II1 * iIIi1iI1II111 % ooo0Oo0 % ii11i
def OOo000 ( title , menu , selection = None ) :
 Oo00OOOOO = - 1
 if selection :
  for OoOoOO00 , O0OO00o0OO in enumerate ( menu ) :
   if selection == O0OO00o0OO [ 0 ] :
    Oo00OOOOO = OoOoOO00
    break
    if 44 - 44: oO0o0o0ooO0oO / iIIi1iI1II111 % I1iII1iiII * ooo0Oo0 + I1II1
 Ii1I = [ ]
 Oo0o0 = [ ]
 for OoOoOO00 , O0OO00o0OO in enumerate ( menu ) :
  Oo = O0OO00o0OO [ 0 ]
  if OoOoOO00 == Oo00OOOOO :
   Oo = '%s' % Oo
  Ii1I . append ( Oo )
  if len ( O0OO00o0OO ) > 2 :
   Oo0o0 . append ( O0OO00o0OO [ 2 ] )
   if 49 - 49: ooo0Oo0 % o000o0o00o0Oo + I1iII1iiII . OOo % i1I1Ii1iI1ii
   if 48 - 48: OOooo0000ooo + OOooo0000ooo / I1Ii111 / ii11i
 if len ( Oo0o0 ) > 0 :
  O0OO00o0OO = i1iiI11I ( title , Ii1I , Oo0o0 , Oo00OOOOO )
 else :
  if Oo00OOOOO > - 1 :
   threading . Timer ( 0 , iiii , [ Oo00OOOOO ] ) . start ( )
   if 54 - 54: i1I1Ii1iI1ii * i1
  O0OO00o0OO = xbmcgui . Dialog ( ) . select ( title , Ii1I )
  if 13 - 13: oO0o0o0ooO0oO + iiIIIII1i1iI - oOooOoO0Oo0O + I1i1I . ii11 + iII1iII1i1iiI
 if O0OO00o0OO < 0 :
  return - 1
  if 8 - 8: ii11i . OOo - ii11i * o000o0o00o0Oo
 return menu [ O0OO00o0OO ] [ 3 ]
 if 61 - 61: iiI11iii111 / iII1iII1i1iiI + OoOoo0 * ooo0Oo0 / ooo0Oo0
 if 75 - 75: I1iII1iiII / oOooOoO0Oo0O - iIIi1iI1II111 / iiIIIII1i1iI . I1Ii111 - I1iII1iiII
def iiii ( index ) :
 if index < 0 :
  return
  if 71 - 71: i1 + o000o0o00o0Oo * i1 - iII1iII1i1iiI * iiI11iii111
 Oooo0Ooo000 = None
 while not Oooo0Ooo000 :
  try :
   Oooo0Ooo000 = xbmcgui . Window ( 12000 )
  except :
   xbmc . sleep ( 50 )
   if 51 - 51: i11iIiiIii . OOo + I1Ii111
 list = None
 while not list :
  try :
   list = Oooo0Ooo000 . getControl ( 3 )
  except :
   xbmc . sleep ( 50 )
   if 10 - 10: i1I1Ii1iI1ii * OoOoo0 * I1Ii111 % o000o0o00o0Oo . i1 + I1i1I
 xbmc . sleep ( 150 )
 list . selectItem ( index )
 if 19 - 19: iiIIIII1i1iI - OOo . i1 / oO0o0o0ooO0oO
def i1iiI11I ( title , options , icons , selectedIndex ) :
 I11II = IiiIII111ii ( 'DialogSelect.xml' , '' , title = title , options = options , icons = icons , selected = selectedIndex )
 I11II . doModal ( )
 O0OO00o0OO = I11II . option
 del I11II
 return O0OO00o0OO
