# Testing

This document is divided into four sections:
<ol>
    <li>Structural Integrity & Responsivity Testing</li>
    <li>Functionality Testing</li>
    <li>Site Navigation Testing</li>
    <li>Form Testing</li>
    <li>Validator Results</li>
    <li>Coverage Report</li>
</ol>
<hr>

## Structural Integrity & Responsivity Testing
<hr>
For these tests, I observed the behaviour of each page of the website, as well as variations of each page, within fourteen device profiles via Google Chrome's developer tools. The devices tested were as follows:
<ul>
    <li>iPhone SE (SE)</li>
    <li>iPhone XR (XR)</li>
    <li>iPhone 12 Pro (12P)</li>
    <li>Google Pixel 5 (P5)</li>
    <li>Samsung Galaxy S8+ (S8+)</li>
    <li>Samsung Galaxy S20 Ultra (S20U)</li>
    <li>iPad Air (A)</li>
    <li>iPad Mini (M)</li>
    <li>Microsoft Surface Pro 7 (SP7)</li>
    <li>Microsoft Surface Duo (SD)</li>
    <li>Samsung Galaxy A51/71 (A51)</li>
    <li>Samsung Galaxy Fold (F)</li>
    <li>Google Nest Hub (NH)</li>
    <li>Google Nest Hub Max (NHM)</li>
</ul>
<hr>
<br>

<strong>Header & dropdown menus - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Header & dropdown menus - logged in as user</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Header & dropdown menus - logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Login page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Sign up page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Verify email address notification page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Confirm email address page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Password reset email address entry page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Password reset email notification page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Change password page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Change password successful notification page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Logout page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Home page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - logged in as user / logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - after search term - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - after search term - logged in as user / logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - sorted - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu page - sorted - logged in as user / logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - logged in as user</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - no reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - some reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - pizza - multiple pages of reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - sides - logged in as superuser</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - sides - logged in as user</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - sides - logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - side - no reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - side - some reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Menu item detail page - side - multiple pages of reviews</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Shopping cart</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Checkout - logged in</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Checkout - logged out</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Checkout success page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - favourite - multiple pages of reviews - multiple pages of messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - no favourite - multiple pages of reviews - multiple pages of messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - favourite - some pages of reviews - some pages of messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - no favourite - some pages of reviews - some pages of messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - favourite - no reviews - no messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Profile page - no favourite - no reviews - no messages</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Order history page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Contact us page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Add item page - no images selected</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Add item page - images selected - warning messages displayed</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<strong>Edit item page</strong>
<table>
    <tr> <th>SE</th> <th>XR</th> <th>12P</th> <th>P5</th> <th>S8+</th> <th>S20U</th> <th>A</th> <th>M</th> <th>SP7</th> <th>SD</th> <th>A51</th> <th>F</th> <th>NH</th> <th>NHM</th> </tr>
    <tr> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> <td>responsive</td> </tr>
</table>
<hr>
<br>

<hr>

## Functionality Testing
<hr>
Much of this aspect of the site has already been tested using automated testing procedures that can be found in each app's directory, but manual testing was still necessary to ensure that the site was <em>visibly</em> changing in response to these interactions. The following functionality was tested and found to be working correctly:
<br>
<br>

### Creating (Menu items, Reviews, and Customer messages)
<ul>
<strong>MENU ITEMS</strong>
    <li>Menu Item added from add item page - appears at bottom of pizza or sides section of menu once approved, and individual page displays when navigated to.</li>
<strong>REVIEWS</strong>
    <li>Review added from individual item page - appears at top of left of first page of review container on same page. Number of reviews of the given score increases by 1, and this is visible in the related tag above the reviews.</li>
<strong>CUSTOMER MESSAGES</strong>
    <li>Customer message added from contact us page - appears at top of first page of messages container on profile page. Number of messages of the given reason increases by 1, and this is visible in the related tag above the messages.</li>
</ul>
<br>

### Updating (Menu items)
<ul>
<strong>MENU ITEMS</strong>
    <li>Existing item edited from edit page - item changes reflected on Menu, on item's individual page, in shopping cart, on checkout page, and in favourite on profile page.</li>
</ul>
<br>

### Deleting (Menu items)
<ul>
<strong>MENU ITEMS</strong>
    <li>Existing menu item deleted from superuser zone on menu page - disappears from menu.</li>
    <li>Existing menu item deleted from superuser zone on its individual page - redirects user to menu page, where the item now cannot be found.</li>
</ul>
<br>

### Favouriting / Unfavouriting (Menu items)
<ul>
<strong>MENU ITEMS</strong>
    <li>Menu item favourited by logged-in user - star turns gold - item appears at top of user's profile page.</li>
    <li>Menu item favourited by non-logged-in user - no visual change - redirected to log in page.</li>
    <li>Menu item favourited by logged-in user - another item favourited by another logged-in user - first item star gold for first user but not for second, and second item star gold for second user but not for first. First user's favourite appears on their profile, and second user's favourite appears on their profile.</li>
</ul>
<hr>
<br>

<hr>

## Site Navigation Testing
<hr>

This particular testing involved trying every link and URL on the site to ensure that they send the user where they are supposed to. To a certain extent, this has been covered by the automated tests I wrote, but I was unable to test that actual buttons and anchor elements were working properly this way, as I was supplying URLs to said tests, rather than testing DOM elements. The following links were tested and were found to be functioning properly:
<br>

### Navbar and header
<ul>
    <li><strong>LOGO LINK</strong></li>
    <li>Logo link directs the user to the home page from the home page (desktop only).</li>
    <li>Logo link directs the user to the home page from the menu page (desktop only).</li>
    <li>Logo link directs the user to the home page from the menu page (search term) (desktop only).</li>
    <li>Logo link directs the user to the home page from the menu page (sorted) (desktop only).</li>
    <li>Logo link directs the user to the home page from a menu item page (pizza) (desktop only).</li>
    <li>Logo link directs the user to the home page from a menu item page (side) (desktop only).</li>
    <li>Logo link directs the user to the home page from the shopping cart (desktop only).</li>
    <li>Logo link directs the user to the home page from the checkout page (desktop only).</li>
    <li>Logo link directs the user to the home page from the checkout success page (desktop only).</li>
    <li>Logo link directs the user to the home page from the user profile page (desktop only).</li>
    <li>Logo link directs the user to the home page from the login page (desktop only).</li>
    <li>Logo link directs the user to the home page from the sign up page (desktop only).</li>
    <li>Logo link directs the user to the home page from the logout page (desktop only).</li>
    <li>Logo link directs the user to the home page from the contact us page (desktop only).</li>
    <li>Logo link directs the user to the home page from the add item page (desktop only).</li>
    <li>Logo link directs the user to the home page from the edit item page (desktop only).</li>
    <li>Logo link directs the user to the home page from the order history page (desktop only).</li>
    <li>Logo link directs the user to the home page from the sign up email notification page (desktop only).</li>
    <li>Logo link directs the user to the home page from the sign up email confirmation page (desktop only).</li>
    <li>Logo link directs the user to the home page from the password reset email form page (desktop only).</li>
    <li>Logo link directs the user to the home page from the password reset email notification page (desktop only).</li>
    <li>Logo link directs the user to the home page from the password reset change password page (desktop only).</li>
    <li>Logo link directs the user to the home page from the password reset password changed notification page (desktop only).</li>
    <li><strong>SEARCH BAR</strong></li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the home page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the menu page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the menu page (search term) (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the menu page (sorted) (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from a menu item page (pizza) (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from a menu item page (side) (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the shopping cart (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the checkout page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the checkout success page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the user profile (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the login page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the sign up page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the logout page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the contact us page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the add item page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the edit item page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the order history page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the sign up email notification page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the sign up email confirmation page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the password reset email form page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the password reset email notification page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the password reset change password page (mobile and desktop).</li>
    <li>The search bar button searches the menu for items matching the search term and displays the search results on the menu page from the password reset password changed page (mobile and desktop).</li>
    <li><strong>HOME BUTTON</strong></li>
    <li>Home button directs the user to the home page from the home page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the menu page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the menu page (search term). (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the menu page (sorted). (mobile and desktop).</li>
    <li>Home button directs the user to the home page from a menu item page (pizza). (mobile and desktop).</li>
    <li>Home button directs the user to the home page from a menu item page (side). (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the shopping cart. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the checkout page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the checkout success page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the user profile page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the login page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the sign up page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the logout page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the contact us page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the add item page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the edit item page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the order history page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the sign up email notification page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the sign up email confirmation page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the password reset email form page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the password reset email notification page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the password reset change password page. (mobile and desktop).</li>
    <li>Home button directs the user to the home page from the password reset password changed notification page. (mobile and desktop).</li>
    <li><strong>PIZZA BUTTON</strong></li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the home page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the menu page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the menu page (search term) (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the menu page (sorted) (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from a menu item page (pizza) (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from a menu item page (side) (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the shopping cart (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the checkout page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the checkout success page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the user profile page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the login page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the sign up page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the logout page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the contact us page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the add item page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the edit item page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the order history page (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the sign up email notification page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the sign up email confirmation page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the password reset email form page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the password reset email notification page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the password reset change password page. (mobile and desktop).</li>
    <li>The pizza button directs the user to the menu page with only pizzas displayed from the password reset password changed notification page. (mobile and desktop).</li>
    <li><strong>SIDES BUTTON</strong></li>
    <li>The sides button directs the user to the menu page with only sides displayed from the home page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the menu page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the menu page (search term) (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the menu page (sorted) (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from a menu item page (pizza) (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from a menu item page (side) (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the shopping cart (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the checkout page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the checkout success page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the user profile page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the login page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the sign up page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the logout page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the contact us page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the add item page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the edit item page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the order history page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the sign up email notification page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the sign up email confirmation page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the password reset email form page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the password reset email notification page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the password reset change password page (mobile and desktop).</li>
    <li>The sides button directs the user to the menu page with only sides displayed from the password reset password changed notification page (mobile and desktop).</li>
    <li><strong>SHOPPING CART BUTTON</strong></li>
    <li>The shopping cart button directs the user to the shopping cart from the home page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the menu page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the menu page (search term) (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the menu page (sorted) (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from a menu item page (pizza) (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from a menu item page (side) (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the shopping cart (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the checkout page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the checkout success page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the user profile page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the login pag (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the sign up page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the logout page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the contact us page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the add item page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the edit item page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the order history page page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the sign up email notification page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the sign up email confirmation page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the password reset email form page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the password reset email notification page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the password reset change password page (mobile and desktop).</li>
    <li>The shopping cart button directs the user to the shopping cart from the password changed notification page (mobile and desktop).</li>
    <li><strong>USER DROPDOWN MENU (SUPERUSER)</strong></li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the home page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the menu page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the menu page (search term) (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the menu page (sorted) (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from a menu item page (pizza)(superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from a menu item page (side) (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the shopping cart (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the checkout page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the checkout success page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the user profile page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the logout page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the contact us page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the add item page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the edit item page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Menu Management, My Profile, and Logout if clicked on from the order history page (superuser only). Clicking again collapses said dropdown (mobile and desktop).</li>
    <li><strong>USER DROPDOWN MENU (NORMAL USER)</strong></li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the home page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the menu page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the menu page (search term) (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the menu page (sorted) (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from a menu item page (pizza)(user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from a menu item page (side) (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the shopping cart (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the checkout page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the checkout success page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the user profile page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the logout page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the contact us page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options My Profile and Logout if clicked on from the order history page (user). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li><strong>USER DROPDOWN MENU (LOGGED OUT)</strong></li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the home page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the menu page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the menu page (search term) (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the menu page (sorted) (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from a menu item page (pizza)(logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from a menu item page (side) (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the shopping cart (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the checkout page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the checkout success page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the login page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the sign up page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the sign up email notification page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the sign up email confirmation page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the password reset email form page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the password reset change password page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the password reset change password page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The user profile button displays a dropdown that includes the options Register and Login if clicked on from the password changed notification page (logged out). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li><strong>FULL MENU DROPDOWN MENU</strong></li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the home page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the menu page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the menu page (search term). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the menu page (sorted). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from a menu item page (pizza). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from a menu item page (side). Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the shopping cart. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the checkout page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the checkout success page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the user profile page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the login page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the sign up page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the logout page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the contact us page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the add item page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the edit item page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the order history page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the sign up email notification page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the sign up email confirmation page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the password reset email form page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the password reset change password page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the password reset change password page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li>The full menu button displays a dropdown that includes the options By Price, By Category, and All Menu Items if clicked on from the password changed notification page. Clicking again collapses said dropdown. (mobile and desktop).</li>
    <li><strong>EXPAND BUTTON DROPDOWN MENU (MOBILE ONLY)</strong></li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the home page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the menu page  (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the menu page (search term) (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the menu page (sorted) (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from a menu item page (pizza) (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from a menu item page (side) (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the shopping cart (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the checkout page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the checkout success page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the user profile page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the login page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the sign up page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the logout page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the contact us page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the add item page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the edit item page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the order history page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the sign up email notification page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the sign up email confirmation page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the password reset email form page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the password reset change password page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the password reset change password page (mobile only). Clicking again collapses said dropdown.</li>
    <li>The expand button displays a dropdown that includes the Home, Pizzas, and Sides buttons, and the Menu Items dropdown if clicked on from the password changed notification page (mobile only). Clicking again collapses said dropdown.</li>
    <li><strong>USER DROPDOWN - REGISTER (LOGGED OUT)</strong></li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the home page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the menu page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the menu page (search term) (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the menu page (sorted) (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from a menu item page (pizza) (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from a menu item page(side) (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the shopping cart (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the checkout page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the checkout success page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the login page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the sign up page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the sign up email notification page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the sign up emil confirmation page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the password reset email form page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the password reset email notification page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the password reset change password page (logged out only) (mobile and desktop).</li>
    <li>The register link in the profile dropdown directs the user to the sign up page from the password reset password changed notification page (logged out only) (mobile and desktop).</li>
    <li><strong>USER DROPDOWN - LOGIN (LOGGED OUT)</strong></li>
    <li>The login link in the profile dropdown directs the user to the log in page from the home page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the menu page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the menu page (search term) (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the menu page (sorted) (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from a menu item page (pizza) (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from a menu item page(side) (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the shopping cart (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the checkout page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the checkout success page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the login page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the sign up page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the sign up email notification page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the sign up emil confirmation page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the password reset email form page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the password reset email notification page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the password reset change password page (logged out only) (mobile and desktop).</li>
    <li>The login link in the profile dropdown directs the user to the log in page from the password reset password changed notification page (logged out only) (mobile and desktop).</li>
    <li><strong>USER DROPDOWN - MENU MANAGEMENT (SUPERUSER ONLY)</strong></li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the home page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the menu page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the menu page (search term) (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the menu page (sorted) (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from a menu item page (pizza) (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from a menu item page(side) (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the shopping cart (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the checkout page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the checkout success page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the user profile page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the logout page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the contact us page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the add item page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the edit item page (superuser only) (mobile and desktop).</li>
    <li>The Menu Management link in the profile dropdown directs the user to the add item page from the order history page (superuser only) (mobile and desktop).</li>
    <li><strong>USER DROPDOWN - MY PROFILE (LOGGED IN)</strong></li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the home page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the menu page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from a menu item page(side) (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the checkout page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the user profile page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the logout page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the contact us page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the add item page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the edit item page (logged in) (mobile and desktop).</li>
    <li>The My Profile link in the profile dropdown directs the user to the user profile page from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>USER DROPDOWN - LOGOUT (LOGGED IN)</strong></li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the home page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the menu page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from a menu item page(side) (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the logout page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the add item page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Logout link in the profile dropdown directs the user to the logout page from the order history page (logged in) (mobile and desktop).</li>  
</ul>

<br>

### Footer
<ul>
    <li><strong>CONTACT US</strong></li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the home page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the menu page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the logout page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the add item page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Contact Us link in the page footer directs the user to the Contact Us page from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>ABOUT US</strong></li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the home page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the menu page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the checkout page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the user profile page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the login page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the sign up page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the logout page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the contact us page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the add item page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the edit item page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the order history page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the sign up email notification page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the sign up email confirmation page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the password reset email form page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the password reset email notification page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the password reset change password page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the password reset password changed notification page (logged in) (mobile and desktop).</li>
    <li>The About Us link in the page footer directs the user to the About Us section of the home page from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>FACEBOOK</strong></li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the home page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the menu page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the login page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the sign up page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the logout page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the add item page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the order history page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the sign up email notification page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the sign up email confirmation page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the password reset email form page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the password reset email notification page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the password reset change password page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the password reset password changed notification page (logged in) (mobile and desktop).</li>
    <li>The Facebook link in the page footer directs the user to the site's Facebook page from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>TWITTER</strong></li>
    <li>The Twitter link in the page footer directs the user to Twitter from the home page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the menu page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the login page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the sign up page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the logout page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the add item page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the order history page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the sign up email notification page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the sign up email confirmation page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the password reset email form page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the password reset email notification page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the password reset change password page (logged in) (mobile and desktop).</li>
    <li>The Twitter link in the page footer directs the user to Twitter from the password reset password changed notification page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>YOUTUBE</strong></li>
    <li>The Youtube link in the page footer directs the user to Youtube from the home page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the menu page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the login page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the sign up page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the logout page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the add item page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the order history page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the sign up email notification page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the sign up email confirmation page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the password reset email form page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the password reset email notification page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the password reset change password page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the password reset password changed notification page (logged in) (mobile and desktop).</li>
    <li>The Youtube link in the page footer directs the user to Youtube from the order history page (logged in) (mobile and desktop).</li>
    <li><strong>INSTAGRAM</strong></li>
    <li>The Instagram link in the page footer directs the user to Instagram from the home page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the menu page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the menu page (search term) (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the menu page (sorted) (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from a menu item page (pizza) (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from a menu item page (side) (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the shopping cart (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the checkout page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the checkout success page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the user profile page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the login page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the sign up page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the logout page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the contact us page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the add item page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the edit item page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the order history page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the sign up email notification page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the sign up email confirmation page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the password reset email form page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the password reset email notification page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the password reset change password page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the password reset password changed notification page (logged in) (mobile and desktop).</li>
    <li>The Instagram link in the page footer directs the user to Instagram from the order history page (logged in) (mobile and desktop).</li>
</ul>

<br>

### Home page
<ul>
    <li>The Menu button directs the user to the Menu page (mobile and desktop).</li>
    <li>The images of the featured pizzas direct the user to their individual pages (mobile and desktop).</li>
    <li>The Order Now buttons on the featured pizzas direct the user to their individual pages (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the home page (mobile and desktop).</li>
</ul>

<br>

### Menu page
<ul>
    <li>Sort By dropdown menu expands to reveal the options Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z), and Category (Z-A). Clicking any option collapses the dropdown and loads a sorted version of the menu page (mobile and desktop).</li>
    <li>Choosing the Price (low to high) sort displays the menu items in order of price, with the cheapest items at the top of the page (mobile and desktop).</li>
    <li>Choosing the Price (high to low) sort displays the menu items in order of price, with the most expensive items at the top of the page (mobile and desktop).</li>
    <li>Choosing the Name (A-Z) sort displays the menu items in alphabetical order, with the lowest letter at the top of the page (mobile and desktop).</li>
    <li>Choosing the Name (Z-A) sort displays the menu items in reverse alphabetical order, with the highest letter at the top of the page (mobile and desktop).</li>
    <li>Choosing the Category (A-Z) sort displays the menu items in the alphabetical order of their categories, with the pizzas at the top of the page (mobile and desktop).</li>
    <li>Choosing the Category (A-Z) sort displays the menu items in the reverse alphabetical order of their categories, with the sides at the top of the page (mobile and desktop).</li>
    <li>Clicking Menu Home from a sorted view of the Menu returns the user to the unsorted Menu (mobile and desktop).</li>
    <li>Clicking Menu Home from Menu search results returns the user to the unsorted Menu (mobile and desktop).</li>
    <li>The images of the pizzas direct the user to their individual pages (mobile and desktop).</li>
    <li>The Order Now buttons on the pizzas direct the user to their individual pages (mobile and desktop).</li>
    <li>The tag links on the pizzas display only the pizzas on the menu (mobile and desktop).</li>
    <li>The images of the sides direct the user to their individual pages (mobile and desktop).</li>
    <li>The Order Now buttons on the sides direct the user to their individual pages (mobile and desktop).</li>
    <li>The tag links on the sides display only the sides on the menu (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the Menu page (mobile and desktop).</li>
    <li>The edit button in the superuser zone on each menu item directs the user to the edit item page (mobile and desktop).</li>
    <li>The delete button in the superuser zone on each menu item deletes that item from the database (mobile and desktop).</li>
    <li>When multiple values are provided for the category query variable in of the url for the Menu page, the resulting view of the menu will include a button for each of those category values. Clicking on one of these displays only those items in that category (mobile and desktop).</li>
</ul>

<br>

### Menu item pages
<ul>
    <li>The favourite button, if is not gold in colour, favourites the item whose page you are on, and un-favourites an item you already had favourited (logged in) (mobile and desktop).</li>
    <li>The favourite button, if is gold in colour, un-favourites the item whose page you are on (logged in) (mobile and desktop).</li>
    <li>The tag link on pizza pages directs the user to the menu page and displays only items in the pizzas category (mobile and desktop).</li>
    <li>The tag link on side pages directs the user to the menu page and displays only items in the sides category (mobile and desktop).</li>
    <li>The size dropdown menu expands to reveal three options: 10'' (Small), 12'' (Medium), and 14'' (Large). Selecting one collapses the dropdown and causes the price text of the item to change accordingly (mobile and desktop).</li>
    <li>The minus quantity button decrements the quantity by 1 unless it is at 1 (mobile and desktop).</li>
    <li>The plus quantity button increments the quantity by 1 unless it is at 99 (mobile and desktop).</li>
    <li>The Keep Shopping button directs the user back to the Menu page (mobile and desktop).</li>
    <li>The Add to Cart button adds the item whose page the user is on to the shopping cart, triggering a message (mobile and desktop).</li>
    <li>The All link above the reviews displays all the reviews for the current item (mobile and desktop).</li>
    <li>The Fantastico link above the reviews displays any and all 5-star reviews for the current item (mobile and desktop).</li>
    <li>The Eccellente link above the reviews displays any and all 4-star reviews for the current item (mobile and desktop).</li>
    <li>The Bene link above the reviews displays any and all 3-star reviews for the current item (mobile and desktop).</li>
    <li>The Brutto link above the reviews displays any and all 2-star reviews for the current item (mobile and desktop).</li>
    <li>The Disgustoso link above the reviews displays any and all 1-star reviews for the current item (mobile and desktop).</li>
    <li>The First button on the pagination controls for the reviews section jumps to the first page of reviews if the user is not already viewing the first page (mobile and desktop).</li>
    <li>The Prev button on the pagination controls for the reviews section goes to the previous page of reviews if the user is not on the first page (mobile and desktop).</li>
    <li>The Next button on the pagination controls for the reviews section goes to the next page of reviews if the user is not on the last page (mobile and desktop).</li>
    <li>The Last button on the pagination controls for the reviews section jumps to the last page of reviews if the user is not already viewing the last page (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the menu item's page (mobile and desktop).</li>
    <li>The edit button in the superuser zone on each menu item directs the user to the edit item page (mobile and desktop).</li>
    <li>The delete button in the superuser zone on each menu item deletes that item from the database (mobile and desktop).</li>
    <li>The dropdown menu on the review form contains 5 selectable options - one for each rating. Choosing one collapses the dropdown menu and displays the user's choice with it (mobile and desktop) (logged in only).</li>
    <li>The post review button on the review form submits the user's review to the page for the given item (mobile and desktop) (logged in only).</li>
</ul>

<br>

### Shopping cart
<ul>
    <li>An item's image directs the user to that item's page when clicked (mobile and desktop).</li>
    <li>The minus quantity button decrements the quantity by 1 unless it is at 1 (mobile and desktop).</li>
    <li>The plus quantity button increments the quantity by 1 unless it is at 99 (mobile and desktop).</li>
    <li>The update button changes the quantity of a given item to the amount set in the quantity field, reloading the shopping cart (mobile and desktop).</li>
    <li>The remove button removes the given item from the shopping cart, reloading the shopping cart (mobile and desktop).</li>
    <li>The Keep Shopping button directs the user back to the Menu page (mobile and desktop).</li>
    <li>The Secure Checkout button directs the user back to the checkout page (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the shopping cart (mobile and desktop).</li>
</ul>

<br>

### Checkout page
<ul>
    <li>The Adjust Cart button directs the user back to the Shopping cart (mobile and dekstop).</li>
    <li>The Complete Order button displays a loading overlay and then directs the user to the checkout success page if the payment was successful, displaying a message (mobile and desktop).</li>
    <li>The images of the items in the order summary direct the user to that item's page when clicked (mobile and desktop).</li>
    <li>If the user is not logged in, the save info checkbox will not be visible, and will be replaced with a message that contains links that direct the user to the Register page and the Login page (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the checkout page (mobile and desktop).</li>
</ul>

<br>

### Checkout success page
<ul>
    <li>The "Now check out the latest deals" button directs the user to the Menu page (mobile and desktop).</li>
</ul>

<br>

### Sign up page (logged out only)
<ul>
    <li>The text at the top of the sign up form contains a link that directs the user to the login page (mobile and desktop).</li>
    <li>The sign up button at the bottom of the form directs the user to a page notifying them that an email has been sent to them containing a link that they must follow to confirm their email address, and generates a message (mobile and desktop).</li>
</ul>

<br>

### Confirm email address for sign up page (logged out only)
<ul>
    <li>The confirm button verifies the user's email address and directs them to the log in page to log in to the site, generating a message (mobile and desktop).</li>
</ul>

<br>

### Log in page (logged out only)
<ul>
    <li>The text at the top of the log in form contains a link that directs the user to the sign up page (mobile and desktop).</li>
    <li>The forgot password link directs the user to a password reset page where they must provide their email address to be sent a link to a page where they can change their password (mobile and desktop).</li>
    <li>The sign in button at the bottom of the form logs the user into their account and directs the user to the home page if they provide the correct credentials, generating a message (mobile and desktop).</li>
</ul>

<br>

### Password reset page - provide email address (logged out only)
<ul>
    <li>The Reset my Password button directs the user to a page notifying them that an email has been sent to them containing a link to a page where they can change their password (mobile and desktop).</li>
</ul>

<br>

### Password reset page - change password (logged out only)
<ul>
    <li>The change password button directs the user to a page notifying them that their password has been successfully changed. A message is generated. (mobile and desktop).</li>
</ul>

<br>

### Logout page (logged in only)
<ul>
    <li>The sign out button signs the user out of their account and directs them to the home page, generating a message (mobile and desktop).</li>
</ul>

<br>

### Contact us page (logged in only)
<ul>
    <li>The dropdown menu on the private message form contains 4 selectable options - one for each kind of message. Choosing one collapses the dropdown menu and displays the user's choice with it (mobile and desktop) (logged in only).</li>
    <li>The send message button on the review form submits the user's private message (mobile and desktop) (logged in only).</li>
</ul>

### User profile page (logged in only)
<ul>
    <li>The favourite section will display if the user has favourited an item on the menu, and the image at its centre will direct them to that item's page if clicked (mobile and desktop).</li>
    <li>The update information button saves whatever the user enters into the delivery information form, and generates a message (mobile and desktop).</li>
    <li>The green order numbers in the order history section direct the user to the order history page for that order, and generates a message (mobile and desktop).</li>
    <li>The All link above the reviews displays all the reviews written by the user for the current item (mobile and desktop).</li>
    <li>The Fantastico link above the reviews displays any and all 5-star reviews written by the user for the current item (mobile and desktop).</li>
    <li>The Eccellente link above the reviews displays any and all 4-star reviews written by the user for the current item (mobile and desktop).</li>
    <li>The Bene link above the reviews displays any and all 3-star reviews written by the user for the current item (mobile and desktop).</li>
    <li>The Brutto link above the reviews displays any and all 2-star reviews written by the user for the current item (mobile and desktop).</li>
    <li>The Disgustoso link above the reviews displays any and all 1-star reviews written by the user for the current item (mobile and desktop).</li>
    <li>The go to links on the user's reviews direct them to the menu item that the given review is a review of (mobile and desktop).</li>
    <li>The First button on the pagination controls for the reviews section jumps to the first page of the user's reviews if the user is not already viewing the first page (mobile and desktop).</li>
    <li>The Prev button on the pagination controls for the reviews section goes to the previous page of the user's reviews if the user is not on the first page (mobile and desktop).</li>
    <li>The Next button on the pagination controls for the reviews section goes to the next page of the user's reviews if the user is not on the last page (mobile and desktop).</li>
    <li>The Last button on the pagination controls for the reviews section jumps to the last page of the user's reviews if the user is not already viewing the last page (mobile and desktop).</li>
    <li>The All link above the private messages displays all the private messages sent by the user (mobile and desktop).</li>
    <li>The Giving feedback link above the messages displays any and all private messages of this kind sent by the user (mobile and desktop).</li>
    <li>The Looking for information link above the messages displays any and all private messages of this kind sent by the user (mobile and desktop).</li>
    <li>The Making a complaint link above the messages displays any and all private messages of this kind sent by the user (mobile and desktop).</li>
    <li>The Other link above the messages displays any and all private messages of this kind sent by the user (mobile and desktop).</li>
    <li>The First button on the pagination controls for the private messages section jumps to the first page of the user's private messages if the user is not already viewing the first page (mobile and desktop).</li>
    <li>The Prev button on the pagination controls for the private messages section goes to the previous page of the user's private messages if the user is not on the first page (mobile and desktop).</li>
    <li>The Next button on the pagination controls for the private messages section goes to the next page of the user's private messages if the user is not on the last page (mobile and desktop).</li>
    <li>The Last button on the pagination controls for the private messages section jumps to the last page of the user's private messages if the user is not already viewing the last page (mobile and desktop).</li>
    <li>The back to top button scrolls to the top of the user profile page (mobile and desktop).</li>
</ul>

<br>

### Add item page (superuser only)
<ul>
    <li>The select image buttons open your computer's File Explorer so that you can browse for an image to select (mobile and desktop).</li>
    <li>The cancel button directs the superuser back to the menu page (mobile and desktop).</li>
    <li>The add menu item button makes a item based on the data in the form and generates a message (mobile and desktop).</li>
</ul>

<br>

<hr>

## Form Testing

<hr>
There are 11 forms on this site: The sign up form, the log in form, the password reset email form, the password change form, the review form, the contact us form, the delivery information form, the payment form, the default delivery information form, the add item form, and the edit item form. I tested each one to ensure that they all submit as they should, and that it isn't possible to submit them if they are incomplete, or supplied with the wrong kind of data.
<hr>

### Sign up form (logged out only)

<ul>
    <li>Cannot be submitted until a valid value has been entered into each field.</li>
    <li>All fields completed but one or both email fields do not match email format - form will not submit.</li>
    <li>All fields completed but username is already taken - form will not submit.</li>
    <li>All fields completed but username is 4 characters or less - form will not submit.</li>
    <li>All fields completed but email addresses do not match - form will not submit.</li>
    <li>All fields completed but passwords do not match - form will not submit.</li>
    <li>All fields completed but passwords are too common / short - form will not submit.</li>
</ul>

<br>

### Log in form (logged out only)

<ul>
    <li>Cannot be submitted until a valid value has been entered into each field.</li>
    <li>All fields completed but email field's value does not match email format - form will not submit.</li>
    <li>All fields completed but email address entered does not exist in database - form will not submit.</li>
    <li>All fields completed but username does not exist in database - form will not submit.</li>
    <li>All fields completed but password is incorrect - form will not submit.</li>
    <li>Remember Me checkbox checked before logging in - login information will be stored in cookies so that the user will still be logged in if they open and close their browser.</li>
</ul>

<br>

### Password reset email form (logged out only)

<ul>
    <li>Email address entered does not match email format - form will not submit.</li>
    <li>Email address entered does not exist in database - form will not submit.</li>
</ul>

<br>

### Password change form (logged out only)

<ul>
    <li>The passwords entered are too short - form will not submit.</li>
    <li>The passwords entered do not match - form will not submit.</li>
    <li>The passwords entered are too common - form will not submit.</li>
</ul>

<br>

### Quantity and size form (menu item page)
<ul>
    <li>Both of the fields in this form are dropdown menus - size and quantity. Neither contain options that cannot be submitted, so it is therefore impossible for this form to fail to submit.</li>
</ul>

<br>

### Review form (logged in only)

<ul>
    <li>A rating from the dropdown menu must be selected, and a review must be written, for the form to submit</li>
    <li>The "Niente..." option in the dropdown menu is selected but the review field has text - form will not submit.</li>
</ul>

<br>

### Contact us form (logged in only)

<ul>
    <li>A rating from the dropdown menu must be selected, and a message must be written, for the form to submit</li>
    <li>The "Choose a reason" option in the dropdown menu is selected but the review field has text - form will not submit.</li>
</ul>

<br>

### Quantity form (shopping cart page)
<ul>
    <li>The quantity selector field in this form does not contain any options that cannot be submitted. Therefore, it is not possible for submission of this form to fail.</li>
</ul>

<br>

### Delivery information form (checkout page)

<ul>
    <li>The following fields are mandatory: Full name, email address, phone number, street address 1, town or city, and country. The form will submit if all of these fields are completed with valid data (along with the payment form; see below). Street address 2, county, state or locality, and postal code can all be left blank, and the form will still submit</li>
    <li>The form will submit if the email address you provide is not the one you registered with.</li>
    <li>Email address entered does not match email format - form will not submit.</li>
</ul>

<br>

### Payment form (checkout page)

<ul>
    <li>The payment form must be completed in addition to the delivery information form in order for the entire checkout page form to successfully submit. You must enter a valid card number, a valid expiry date, a CVC number, and a ZIP code. The form alerts you in real-time if the card number you are entering is invalid.</li>
</ul>

<br>

### Default delivery information form (profile page / logged in only)

<ul>
    <li>None of the fields on this form are mandatory. A blank form can be submitted. This will be reflected in the delivery information form at the checkout page.</li>
</ul>

<br>

### Add item form (logged in as superuser only)

<ul>
    <li>The name, calories, and price fields are mandatory, but the description, ingredients, and image fields are optional. The form can be submitted without filling in said optional fields. Any of the options in the category and has sizes dropdown menus can be submitted.</li>
    <li>There are no limits to what size the images can be, but a warning message will appear when you select one that contains the suggested dimensions.</li>
</ul>

<br>

### Edit item form (logged in as superuser only)

<ul>
    <li>The name, calories, and price fields are mandatory, but the description, ingredients, and image fields are optional. The form can be submitted without filling in said optional fields. Any of the options in the category and has sizes dropdown menus can be submitted. Existing optional values can be removed, and the form will still submit successfully.</li>
    <li>There are no limits to what size the images can be, but a warning message will appear when you select one that contains the suggested dimensions.</li>
</ul>

<br>

<hr>

## Validator Results

<hr>

### W3C (HTML validation)
<br>
Inde\x page (not logged in): <img src="static/images/index-not-logged-in-validated.png" alt="An image of base.html / index.html (not logged in) passing validation.">
Index page (logged in): <img src="static/images/index-logged-in-validated.png" alt="An image of base.html / index.html (logged in) passing validation.">
Bulletin page (not logged in): <img src="static/images/bulletin-page-not-logged-in-validated.png" alt="An image of base.html / bulletin.html (not logged in) passing validation.">
Bulletin page (logged in): <img src="static/images/bulletin-page-logged-in-validated.png" alt="An image of base.html / bulletin.html (logged in) passing validation.">
Add Bulletin page: <img src="static/images/add-bulletin-page-validated.png" alt="An image of base_alt.html / add_bulletin.html passing validation.">
Edit Bulletin page: <img src="static/images/edit-bulletin-page-validated.png" alt="An image of base_alt.html / edit_bulletin.html passing validation.">
Edit Comment page: <img src="static/images/edit-comment-page-validated.png" alt="An image of base.html / add_bulletin.html during comment editing passing validation.">
Sign Up page: <img src="static/images/sign-up-page-validated.png" alt="An image of base_alt.html / signup.html passing validation.">
Sign In page: <img src="static/images/sign-in-page-validated.png" alt="An image of base_alt.html / login.html passing validation.">
Sign Out page: <img src="static/images/sign-out-page-validated.png" alt="An image of base_alt.html / logout.html passing validation.">
<br>
<hr>
<br>

### Jigsaw (CSS validation)
<br>
style.css validation: <img src="static/images/css-validated.png" alt="An image of style.css passing validation.">
Warnings about use of vendor extensions: <img src="static/images/css-validated-warnings.png" alt="An image of warnings from the same results as the image above.">
<br>
<hr>
<br>

<hr>

## Coverage Report
<hr>
<br>
<img src="static/images/coverage-report.png" alt="An image of the coverage report for my app's Python code.">