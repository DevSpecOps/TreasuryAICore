using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddHealthChecks();

var app = builder.Build();

app.MapGet("/api/v1/payment/health", () => new { status = "UP", service = "payment-service" });
app.MapControllers();

app.Run();