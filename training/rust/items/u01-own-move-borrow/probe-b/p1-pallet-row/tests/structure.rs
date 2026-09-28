use u01_probe_b_p1::Pallet;

// Compiles only while `Pallet` is not `Copy`. If it were `Copy`, the call below
// would match both impls and the compiler would refuse it as ambiguous.
trait CopyProbe<Marker> {
    fn probe() {}
}

impl<T> CopyProbe<()> for T {}

struct WhenCopy;

impl<T: Copy> CopyProbe<WhenCopy> for T {}

#[test]
fn pallet_is_not_copy() {
    <Pallet as CopyProbe<_>>::probe();
}
