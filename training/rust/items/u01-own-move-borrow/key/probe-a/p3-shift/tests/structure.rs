use u01_probe_a_p3::Point;

// Compiles only while `Point` is not `Copy`. If it were `Copy`, the call below
// would match both impls and the compiler would refuse it as ambiguous.
trait CopyProbe<Marker> {
    fn probe() {}
}

impl<T> CopyProbe<()> for T {}

struct WhenCopy;

impl<T: Copy> CopyProbe<WhenCopy> for T {}

#[test]
fn point_is_not_copy() {
    <Point as CopyProbe<_>>::probe();
}
