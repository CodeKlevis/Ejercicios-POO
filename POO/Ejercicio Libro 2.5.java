public class CuentaBancaria {
    String nombresTitular;
    String apellidosTitular;
    int numeroCuenta;
    enum tipo {AHORROS, CORRIENTE}
    tipo tipoCuenta;
    float saldo = 0;

    CuentaBancaria(String nombresTitular, String apellidosTitular, int numeroCuenta, tipo tipoCuenta) {
        this.nombresTitular = nombresTitular;
        this.apellidosTitular = apellidosTitular;
        this.numeroCuenta = numeroCuenta;
        this.tipoCuenta = tipoCuenta;
    }

    void imprimir() {
        System.out.println("Nombres del titular = " + nombresTitular);
        System.out.println("Apellidos del titular = " + apellidosTitular);
        System.out.println("Número de cuenta = " + numeroCuenta);
        System.out.println("Tipo de cuenta = " + tipoCuenta);
        System.out.println("Saldo = " + saldo);
    }

    void consultarSaldo() {
        System.out.println("El saldo actual es = " + saldo);
    }

    boolean consignar(int valor) {
        if (valor > 0) {
            saldo = saldo + valor;
            System.out.println("Se ha consignado $" + valor + " en la cuenta. El nuevo saldo es $" + saldo);
            return true;
        } else {
            System.out.println("El valor a consignar debe ser mayor que cero.");
            return false;
        }
    }

    boolean retirar(int valor) {
        if ((valor > 0) && (valor <= saldo)) {
            saldo = saldo - valor;
            System.out.println("Se ha retirado $" + valor + " en la cuenta. El nuevo saldo es $" + saldo);
            return true;
        } else {
            System.out.println("El valor a retirar debe ser menor o igual al saldo actual.");
            return false;
        }
    }

    boolean compararCuentas(CuentaBancaria cuenta) {
        return this.numeroCuenta == cuenta.numeroCuenta;
    }

    boolean transferencia(CuentaBancaria cuenta, int valor) {
        if (retirar(valor)) {
            cuenta.consignar(valor);
            System.out.println("Se ha transferido $" + valor + " a la cuenta " + cuenta.numeroCuenta);
            return true;
        } else {
            System.out.println("No se pudo realizar la transferencia.");
            return false;
        }
    }

    public static void main(String args[]) {
        CuentaBancaria cuenta1 = new CuentaBancaria("Pedro", "Pérez", 123456789, tipo.AHORROS);
        CuentaBancaria cuenta2 = new CuentaBancaria("Juan", "Gómez", 987654321, tipo.CORRIENTE);

        cuenta1.imprimir();
        cuenta1.consignar(200000);
        cuenta1.retirar(50000);
        cuenta1.consultarSaldo();

        System.out.println("¿Las cuentas son iguales? " + cuenta1.compararCuentas(cuenta2));

        cuenta1.transferencia(cuenta2, 100000);
        cuenta2.consultarSaldo();
    }
}
