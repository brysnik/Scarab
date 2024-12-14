#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    let _ = run_python();
    "Hello, world!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}

use pyo3::types::IntoPyDict;
use pyo3::Python;
use pyo3::PyResult;
use pyo3::prelude::PyAnyMethods;

fn run_python() -> PyResult<()> {
    Python::with_gil(|py| {
        let sys = py.import("sys")?;
        let os = py.import("os")?;
        let version: String = sys.getattr("version")?.extract()?;
        let user: String = os.call_method0("getlogin")?.extract()?;

        println!("Hello {}, I'm Python {}", user, version);
        Ok(())
    })
}
