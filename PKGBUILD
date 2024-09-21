# Maintainer
pkgname=whatsapp-fl
pkgver=1.0
pkgrel=1
pkgdesc="Una aplicación de WhatsApp para Linux."
arch=('any')
url="https://github.com/CarlosNavarroUTD/whatsapp_for_arch.git"
license=('MIT')  # Cambia esto según tu licencia
depends=('python' 'python-pip')  # Agrega más dependencias si es necesario
source=(
    'app.py'
    'launch_whatsapp.sh'
    'requirements.txt'
)
md5sums=('SKIP' 'SKIP' 'SKIP')  # Puedes generar sumas de verificación para mayor seguridad

package() {
    install -Dm755 "$srcdir/app.py" "$pkgdir/usr/bin/$pkgname"
    install -Dm755 "$srcdir/launch_whatsapp.sh" "$pkgdir/usr/bin/launch_whatsapp"
    install -Dm644 "$srcdir/requirements.txt" "$pkgdir/usr/share/$pkgname/requirements.txt"
}
